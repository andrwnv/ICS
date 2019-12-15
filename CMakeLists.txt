cmake_minimum_required(VERSION 3.5)

project(ICS)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

find_package(Qt5 COMPONENTS Widgets Core REQUIRED)

find_package(SQLite3)
include_directories(${SQLite3_INCLUDE_DIRS})

add_executable(ICS
               main.cpp
               IndustrialControlSystem.cpp
               IndustrialControlSystem.h
)

target_link_libraries(ICS PRIVATE Qt5::Widgets ${SQLite3_INCLUDE_DIRS})
