""" Test driver for CMake integration tests.

This will verify that the library is usable by another CMake project as an
external build tree or an installed library.

"""
from argparse import ArgumentParser
from pathlib import Path
from subprocess import Popen, PIPE, STDOUT, check_call
from sys import stdout
from tempfile import TemporaryDirectory


def main() -> int:
    """ Build the C++ test application and execute it.

    :return: exit status (0 on success)
    """
    parser = ArgumentParser()
    parser.add_argument("type", help="test type")
    parser.add_argument("root", help="project root directory", nargs="?", default=Path.cwd())
    args = parser.parse_args()
    with TemporaryDirectory() as test_dir:
        test_dir = Path(test_dir)
        defines = {
            "CMAKE_BUILD_TYPE": "Release",
        }
        build_dir = test_dir / "build"
        install_dir = test_dir / "usr/local"
        if args.type.lower() == "source":
            # Test source tree build.
            defines["LIBRARY_SOURCE_DIR"] = args.root
        elif args.type.lower() == "install":
            # Test installed library.
            source_dir = Path(args.root)
            defines["CMAKE_PREFIX_PATH"] = install_dir
            defines["CMAKE_INSTALL_PREFIX"] = install_dir
            _build(source_dir, build_dir / "lib", defines, "install")
        else:
            raise ValueError(f"unknown test type: {args.type}")
        local_dir = Path(__file__).parent / "libtest"
        _build(local_dir, build_dir, defines)
        check_call([str(build_dir / "libtest")])
    return 0


def _build(source: Path, build: Path, defs: dict, target=None):
    """ Build a CMake project.

    :param source: source directory
    :param build: build directory
    :param defs: CMake definitions
    :param target: target name
    """
    def cmake(*args):
        """ Execute `cmake` command. """
        argv = ["cmake"] + list(map(str, args))
        process = Popen(argv, stdout=PIPE, stderr=STDOUT)
        for line in iter(process.stdout.readline, b""):
            # Echo command's stdout and stderr to terminal.
            stdout.write(line.decode())
        process.wait()
        if process.returncode != 0:
            raise RuntimeError(f"cmake failed: {process.returncode}")
        return process.returncode

    config_args = [f"-D{key}={value}" for key, value in defs.items()]
    config_args.extend(("-S", source, "-B", build))
    cmake(*config_args)
    build_args = ["--build", build]
    if target:
        build_args.extend(("--target", target))
    cmake(*build_args)
    return


if __name__ == "__main__":
    raise SystemExit(main())
