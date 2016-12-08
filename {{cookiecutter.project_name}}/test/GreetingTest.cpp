/// Test suite for the Greeting class.
///
#include <string>
#include "gtest/gtest.h"

#include "hello.hpp"


using namespace testing;
using namespace Hello;


/// Test fixture for the Greeting class.
///
/// This is used to group tests and provide common set-up and tear-down code.
/// A new test fixture is created for each test to prevent any side effects
/// between tests. Member variables and methods are injected into each test
/// that uses this fixture as if it's a derived class method.
///
class GreetingTest : public Test
{
protected:
    const Greeting english;
    const Greeting spanish;
    GreetingTest() : english("Hello"), spanish("Hola") {}
    virtual ~GreetingTest() { /* Tear-down code goes here. */ }
};


/// Test an English greeting.
///
TEST_F(GreetingTest, english) {
    ASSERT_EQ("Hello, World!", english());
}


/// Test a Spanish greeting.
///
TEST_F(GreetingTest, spanish) {
    ASSERT_EQ("Hola, Mundo!", spanish("Mundo"));
}
