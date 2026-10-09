"""
Exercise 3 - Software Design | Task 1: Abstract Base Class Interfaces
=================================================================================
"""

from abc import ABC, abstractmethod


#  TODO: 1.1 - 1.3: a plain base class
class ...


#  TODO: 1.4: an abstract base class = an interface
class ...


#  TODO: 1.5: no base class at all
class ...


#  TODO: High-level code: depends only on the interface
def check_distance...


if __name__ == "__main__":
    print("\n1.2  check_distance(Radar())")
    check_distance(Radar())

    # print("\n1.3  check_distance(Camera())")
    # check_distance(Camera())

    # print("\n1.4  check_distance(Lidar())  and  check_distance(Ultrasonic())")
    # check_distance(Lidar())
    # try:
    #     check_distance(Ultrasonic())
    # except TypeError as error:
    #     print(f"TypeError: {error}")
    # try:
    #     DistanceSensor()
    # except TypeError as error:
    #     print(f"TypeError: {error}")

    # print("\n1.5  check_distance(V2XReceiver())")
    # check_distance(V2XReceiver())
