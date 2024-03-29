""" Test the Cookiecutter template.

"""
import pytest
from cookiecutter.generate import generate_context
from cookiecutter.main import cookiecutter
from pathlib import Path
from shlex import split
from subprocess import check_call, run


@pytest.fixture(scope="session")
def template() -> Path:
    """ The template under test.

    """
    return Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session")
def tmpdir(tmp_path_factory) -> Path:
    """ Session test directory.

    """
    # Replace builtin `tmpdir` to provide session scope.
    return tmp_path_factory.mktemp("test_template")


@pytest.fixture(scope="session")
def context(template) -> dict:
    """ Template context for testing.

    """
    context = generate_context(template.joinpath("cookiecutter.json"))
    context["cookiecutter"] |= {
        "project_slug": "cpplib"
    }
    return context["cookiecutter"]


@pytest.fixture(scope="session")
def project(tmpdir, template, context) -> Path:
    """ Create a test project from the Cookiecutter template.

    """
    cookiecutter(str(template), no_input=True, output_dir=tmpdir, extra_context=context)
    return tmpdir / context["project_slug"]


@pytest.fixture(scope="session")
def build(project) -> Path:
    """ Build the project.

    :return: build root path
    """
    root = "build/Debug"
    check_call(split(f"make BUILD_ROOT={root} dev build"), cwd=project)
    return project / root


def test_project(project):
    """ Verify that the project was created correctly.

    """
    # Just a basic sanity test.
    assert len(list(project.iterdir())) == 11
    return


@pytest.mark.usefixtures("build")
def test_unit(project):
    """ Verify that unit tests are working.

    """
    process = run(split(f"make test"), cwd=project)
    assert process.returncode == 0
    return


def test_install(tmp_path, project, context, build):
    """ Test the installation rules.

    """
    install = tmp_path / "usr/local"
    command = f"cmake --install {build} --prefix {install}"
    process = run(split(command), cwd=project)
    assert process.returncode == 0
    lib = f"lib{context['lib_name']}.a"  # TODO: make this portable
    assert Path(install / "lib" / lib).is_file()
    assert Path(install / "include" / context['lib_name']).is_dir()
    return


@pytest.mark.usefixtures("build")
def test_docs(project):
    """ Verify documentation build.

    """
    process = run(split(f"make docs"), cwd=project)
    assert process.returncode == 0
    path = Path(project / "docs/doxygen/html")
    assert next(path.iterdir())  # directory isn't empty
    return


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
