cmake_minimum_required(VERSION 3.5)

project(ICS)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt5 COMPONENTS Widgets Core REQUIRED)

add_executable(ICS
               main.cpp
               IndustrialControlSystem.cpp
               IndustrialControlSystem.h
)

target_link_libraries(ICS PRIVATE Qt5::Widgets)
