""" Integration tests.

This will verify that the library is usable by another CMake project as an
external build tree or an installed library.

"""
import pytest
from pathlib import Path
from subprocess import Popen, PIPE, run, STDOUT
from sys import stdout
from shlex import split


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


@pytest.fixture
def build_dir(tmp_path) -> Path:
    """ Return a temporary build directory.

    :return: build directory path
    """
    return tmp_path / "build"


@pytest.fixture
def install(tmp_path, build_dir) -> dict:
    """ Configure the build to use an installed library.

    :return: CMake definitions
    """
    source_dir = Path.cwd()
    install_dir = tmp_path / "usr/local"
    defs = {
        "BUILD_TESTING": "OFF",
        "CMAKE_PREFIX_PATH": install_dir,
        "CMAKE_INSTALL_PREFIX": install_dir,
    }
    _build(source_dir, build_dir / "lib", defs, "install")
    return defs


@pytest.fixture
def source() -> dict:
    """ Configure the build to the library source tree.

    :return: CMake definitions
    """
    return {
        "BUILD_TESTING": "OFF",
        "LIBRARY_SOURCE_DIR": Path.cwd(),
    }


@pytest.fixture(params=("install", "source"))
def app(request, build_dir) -> Path:
    """ Build the C++ test application.

    :return: application path
    """
    defs = request.getfixturevalue(request.param)
    defs |= {"CMAKE_BUILD_TYPE": "Release"}
    local_dir = Path(__file__).parent / "libtest"
    _build(local_dir, build_dir, defs)
    return build_dir / "libtest"


def test_lib(app):
    """ Test the library as part of an application.

    """
    process = run(split(str(app)), capture_output=True)
    assert process.returncode == 0
    return


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
