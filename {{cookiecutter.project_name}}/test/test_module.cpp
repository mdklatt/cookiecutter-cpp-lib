/// Test suite for the sample module.
///
/// Link all test files with the `gtest_main` library to create a command-line 
/// test runner.
///
#include <gtest/gtest.h>
#include "module.hpp"

using namespace {{ cookiecutter.lib_name }};


/// Test a sample function call.
///
TEST(add, test)
{
    ASSERT_EQ(3, add(1, 2));
}
