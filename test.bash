## Test the cpp-lib Cookiecutter template.
##
## A template project is created in a temporary directory, the library and its
## test suite are built, and the test suite is executed.
##
set -e  # exit immediately on failure
if [[ "$(uname)" == "Darwin" ]]
then  # OS X uses BSD mktemp
    MKTEMP="mktemp -d -t tmp"
else  # assume Linux/GNU or similar
    MKTEMP="mktemp -d"
fi
template=$(pwd)
tmpdir=$(${MKTEMP})
trap "rm -rf $tmpdir" EXIT  # remove on exit
pushd $tmpdir
cookiecutter $template --no-input
cd hello
cmake -DCMAKE_BUILD_TYPE=Debug && make
build/Debug/test_hello
popd
exit 0
