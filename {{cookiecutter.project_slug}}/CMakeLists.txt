cmake_minimum_required(VERSION {{ cookiecutter.cmake_version }})

project({{ cookiecutter.lib_name }}
    VERSION {{ cookiecutter.project_version }}  # add build number to designate a dev version
    LANGUAGES CXX
)

option(BUILD_DOCS "Build documentation" OFF)

set(name ${PROJECT_NAME})
set(CMAKE_CXX_STANDARD {{ cookiecutter.cpp_standard }})
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_subdirectory(src)

include(GNUInstallDirs)

install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})


# Including CTest here at the project root makes `ctest` runnable from the
# build root. This is also necessary for CLion to generate a CTest Run
# Configuration.
include(CTest)
if(BUILD_TESTING)  # defined by CTest module
    add_subdirectory(tests)
endif()

if(BUILD_DOCS)
    add_subdirectory(docs)
endif()
