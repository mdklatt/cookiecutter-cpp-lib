## CMake build file for the {{ cookiecutter.lib_name }} library.
##
## This will build the library and its test suite. Compiled binaries will be
## written to build/${CMAKE_BUILD_TYPE}.
##
cmake_minimum_required(VERSION 2.8.12)

project({{ cookiecutter.lib_name }})

set(LIB_FILES
    ${CMAKE_SOURCE_DIR}/src/module.cpp
)

set(CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS} "-std=c++11 -Wall")
#include_directories(src)
add_library(${PROJECT_NAME} ${LIB_FILES})

function(install)
    # Disable install for test directory.
endfunction()
add_subdirectory(test)
