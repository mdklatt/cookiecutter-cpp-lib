/**
 * Verify that the library is usable in an external CMake project by testing
 * that all headers are present and all modules are linkable.
 */
#include "{{ cookiecutter.lib_name }}/module.hpp"


/**
 * Execute the application.
 *
 * @return system exit status
 */
int main() {
    return {{ cookiecutter.lib_name }}::add(1, 2) == 3 ? 0 : 1;
}
