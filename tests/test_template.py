""" Test the Cookiecutter template.

A template project is created in a temporary directory, the library and its
test suite are built, and the test suite is executed.

"""
from json import loads
from pathlib import Path
from shlex import split
from subprocess import check_call
from tempfile import TemporaryDirectory

from cookiecutter.main import cookiecutter


def main() -> int:
    """ Execute the test.
    
    """
    template = Path(__file__).resolve().parents[1]
    defaults = loads(template.joinpath("cookiecutter.json").read_text())
    with TemporaryDirectory() as tmpdir:
        cookiecutter(str(template), no_input=True, output_dir=tmpdir)
        name = defaults["lib_name"]
        cwd = Path(tmpdir) / name
        for opts in "-DCMAKE_BUILD_TYPE=Debug", "--build":
            check_call(split(f"cmake {opts:s} ."), cwd=cwd)
        check_call(split(f"tests/unit/test_{name:s}"), cwd=cwd)
    return 0
    
    
# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
