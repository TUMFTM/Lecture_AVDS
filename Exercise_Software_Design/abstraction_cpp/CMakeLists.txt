cmake_minimum_required(VERSION 3.8)
project(abstraction_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)

add_executable(base_class_interface src/base_class_interface.cpp)
target_include_directories(base_class_interface PRIVATE include)
target_compile_features(base_class_interface PRIVATE cxx_std_17)

install(TARGETS base_class_interface
  DESTINATION lib/${PROJECT_NAME})

ament_package()
