## CMake build file for the {{ cookiecutter.lib_name }} library.
##
cmake_minimum_required(VERSION 3.8)

project({{ cookiecutter.lib_name }}
    VERSION {{ cookiecutter.project_version }}
    LANGUAGES CXX
)

# Define project targets.

add_library(${PROJECT_NAME}
    src/module.cpp
)

target_include_directories(${PROJECT_NAME}
PUBLIC
    # Interface paths are relative to the installation path, not the current
    # directory.
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/src
)

target_compile_features(${PROJECT_NAME}
PUBLIC
    cxx_std_11
)

target_compile_options(${PROJECT_NAME}
PRIVATE
    -Wall
    $<$<CXX_COMPILER_ID:GNU>:-pedantic>
)


# Add subdirectories to build.

add_subdirectory(test)
