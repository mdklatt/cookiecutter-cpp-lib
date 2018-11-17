""" Perform post-generation tasks.

This is executed in the new project directory. Before execution it is rendered 
with the template engine, so it has access to all template variables.

"""
from os import renames
from os.path import join
from tempfile import TemporaryDirectory
from urllib.request import urlopen
from zipfile import ZipFile


def get_googletest():
    """ Download Google Test from GitHub.
    
    Google recommends that each project maintains its own version of this
    library, compiled with the same flags as the project to avoid potential
    violations of the One-Definition Rule.
    
    """
    download = "https://github.com/google/googletest/archive/{:s}.zip"
    release = "{{ cookiecutter.googletest_release }}"
    print("downloading Google Test ({:s})".format(release))
    if release != "master":
        release = "release-{:s}".format(release)
    libroot = join("test", "vendor", "googletest")
    with TemporaryDirectory() as tmpdir:
        # Extract the downloaded zip file to a temporary directory. ZipFile
        # requires a stream with a seek() method, so the archive must be
        # downloaded to a local file first.
        stream = open(join(tmpdir, "googletest.zip"), "w+b")
        print(download.format(release))
        stream.write(urlopen(download.format(release)).read())
        archive = ZipFile(stream, mode="r")
        archive.extractall(tmpdir)
        renames(join(tmpdir, "googletest-{:s}".format(release)), libroot)
    return


def main():
    """ Execute all tasks. 
    
    """
    get_googletest()
    return 0


# Make the script executable from the command line.

if __name__ == "__main__":
    raise SystemExit(main())
