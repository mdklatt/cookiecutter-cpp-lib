/// Implementation of the Greeting class.
///
#include "Greeting.hpp"


using namespace std;
using namespace Hello;


/// Return a greeting message.
///
string Greeting::operator()(const string& name) const
{
    return hello_ + ", " + name + "!";
}
