## CMake build file for the {{ cookiecutter.repo_name }} library test suite.
##
## This will build a Google Test test runner for all contained tests.
##
project(test_{{ cookiecutter.repo_name }})

add_subdirectory(lib/gtest)

include_directories(${gtest_SOURCE_DIR} ${gtest_SOURCE_DIR}/include)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/build/${CMAKE_BUILD_TYPE})

add_executable(${PROJECT_NAME} GreetingTest.cpp)
target_link_libraries(${PROJECT_NAME} {{ cookiecutter.repo_name }} gtest gtest_main)
