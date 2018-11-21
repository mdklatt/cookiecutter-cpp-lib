## Build the {{ cookiecutter.lib_name }} library.
##
cmake_minimum_required(VERSION 3.8)

project({{ cookiecutter.lib_name }}
    VERSION {{ cookiecutter.project_version }}
    LANGUAGES CXX
)

# Define project targets.

add_library({{ cookiecutter.lib_name }}
    src/module.cpp
)
add_library({{ cookiecutter.lib_name }}::{{ cookiecutter.lib_name }} ALIAS {{ cookiecutter.lib_name }})

target_include_directories({{ cookiecutter.lib_name }}
PUBLIC
    # Interface paths are relative to the installation path, not the current
    # directory.
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/src
)

target_compile_features({{ cookiecutter.lib_name }}
PUBLIC
    cxx_std_11
)

target_compile_options({{ cookiecutter.lib_name }}
PRIVATE
    -Wall
    $<$<CXX_COMPILER_ID:GNU>:-pedantic>
)


# Generate package config files.

include(CMakePackageConfigHelpers)

configure_package_config_file(
    ${CMAKE_CURRENT_LIST_DIR}/cmake/{{ cookiecutter.lib_name }}-config.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/{{ cookiecutter.lib_name }}-config.cmake
INSTALL_DESTINATION
    ${CMAKE_INSTALL_LIBDIR}/cmake/{{ cookiecutter.lib_name }}
)

write_basic_package_version_file(
    ${CMAKE_CURRENT_BINARY_DIR}/{{ cookiecutter.lib_name }}-config-version.cmake
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY AnyNewerVersion
)


# Define installation rules.

include(GNUInstallDirs)

install(
TARGETS 
    {{ cookiecutter.lib_name }}
EXPORT {{ cookiecutter.lib_name }}-targets
LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

install(DIRECTORY include/
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

install(
FILES
    ${CMAKE_CURRENT_BINARY_DIR}/{{ cookiecutter.lib_name }}-config.cmake
    ${CMAKE_CURRENT_BINARY_DIR}/{{ cookiecutter.lib_name }}-config-version.cmake
DESTINATION
    ${CMAKE_INSTALL_LIBDIR}/cmake/{{ cookiecutter.lib_name }}
)

install(EXPORT {{ cookiecutter.lib_name }}-targets
    FILE {{ cookiecutter.lib_name }}-targets.cmake
    NAMESPACE {{ cookiecutter.lib_name }}::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/{{ cookiecutter.lib_name }}
)


# Export targets. If an external project adds this project to its build tree
# via `add_subdirectory()`, then `find_package()` will work without
# requiring this project to be installed.

export(EXPORT {{ cookiecutter.lib_name }}-targets
    FILE ${CMAKE_CURRENT_BINARY_DIR}/{{ cookiecutter.lib_name }}-targets.cmake
    NAMESPACE {{ cookiecutter.lib_name }}::
)
export(PACKAGE {{ cookiecutter.lib_name }})


# Add subdirectories to build.

add_subdirectory(test)
