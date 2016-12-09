/// Implementation of the sample library module.
///
#include "module.hpp"

using namespace {{ cookiecutter.lib_name }};


int SampleClass::add(int x) const
{
    return ::add(num, x);
}


int {{ cookiecutter.lib_name }}::add(int x, int y)
{
    return x + y;
}
