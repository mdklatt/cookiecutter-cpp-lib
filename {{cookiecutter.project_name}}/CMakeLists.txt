## CMake build file for the {{ cookiecutter.lib_name }} library.
##
## This will build the library and its test suite. Compiled binaries will be
## written to build/${CMAKE_BUILD_TYPE}.
##
cmake_minimum_required(VERSION 3.0)
project({{ cookiecutter.lib_name }})

set(CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS} "-std=c++11 -Wall")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/build/${CMAKE_BUILD_TYPE})
set(SOURCE_FILES src/module.cpp)
include_directories(src)
add_library(${PROJECT_NAME} ${SOURCE_FILES})
add_subdirectory(test)
