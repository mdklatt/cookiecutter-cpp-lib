/**
 * Implementation of the sample library module.
 */
#include "{{ cookiecutter.lib_name }}/module.hpp"

using {{ cookiecutter.lib_name }}::SampleClass;


int SampleClass::add(int x) const {
    return {{ cookiecutter.lib_name }}::add(num, x);
}


int {{ cookiecutter.lib_name }}::add(int x, int y) {
    return x + y;
}
