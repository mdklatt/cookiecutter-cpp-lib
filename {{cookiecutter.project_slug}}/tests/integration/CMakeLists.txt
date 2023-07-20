# Verify that the installed libraries are usable to downstream applications via
# CMake. The sample application 'libtest' is built using both the project
# tree and an installed version.

# Give find_package() some help locating the correct Python executable.
set(Python3_EXECUTABLE "$ENV{SYSTEM_PYTHON}")
set(python_min_version 3.9)
find_package(Python3 ${python_min_version} COMPONENTS Interpreter)
if (NOT Python3_FOUND)
    message(WARNING "Skipping integration tests; requires Python ${python_min_version}+")
    return()
endif()

message(STATUS "Enabling integration tests using ${Python3_EXECUTABLE}")
set(test_types source install)
foreach(type ${test_types})
    add_test(
        NAME "integration_${type}_build"
        COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_integration.py ${type}
        WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
    )
endforeach()
