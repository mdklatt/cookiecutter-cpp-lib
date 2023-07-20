cmake_minimum_required(VERSION {{ cookiecutter.cmake_version }})
project(libtest LANGUAGES CXX)

set(CMAKE_CXX_STANDARD {{ cookiecutter.cpp_standard }})
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(IS_DIRECTORY ${LIBRARY_SOURCE_DIR})
    # This uses the existing project directory, so uncommitted changes may hide
    # errors that would occur in a clean checkout.
    message(STATUS "Testing library build tree at ${LIBRARY_SOURCE_DIR}")
    add_subdirectory(${LIBRARY_SOURCE_DIR} ${CMAKE_CURRENT_BINARY_DIR}/lib)
else()
    # All default search locations are disabled to ensure that only the test
    # installation is found.
    message(STATUS "Testing installed library at ${path}")
    list(APPEND CMAKE_MODULE_PATH "${CMAKE_PREFIX_PATH}/cmake")
    message(STATUS "CMAKE_MODULE_PATH: ${CMAKE_MODULE_PATH}")
    find_package({{ cookiecutter.lib_name }} REQUIRED)
endif()
    

add_executable(libtest libtest.cpp)
target_link_libraries(libtest
PRIVATE
    {{ cookiecutter.lib_name }}::{{ cookiecutter.lib_name }}
)
