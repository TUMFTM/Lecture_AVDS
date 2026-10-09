# Workflow
## Option 1
One file.
### Build
```g++ -O3 -I abstraction_cpp/include abstraction_cpp/src/base_class_interface.cpp -o my_program```

### Run
```./my_program```

## Option 2 (CMake)
One package.
### Build
```cmake -S abstraction_cpp -B build```\
```cmake --build build```

### Run
```./build/base_class_interface```

## Option 3 (ROS 2)
The whole workspace.
### Build
```colcon build```\
```source install/setup.bash```

### Run
```ros2 run abstraction_cpp base_class_interface```

or

```./install/abstraction_cpp/lib/abstraction_cpp/base_class_interface```