"""
Exercise 3 - Software Design | Task 1: Abstract Base Class Interfaces  (SOLUTION)
=================================================================================

The ACC needs the distance to the vehicle ahead. Whether it comes from a radar,
a lidar or a camera should not matter to the ACC: that is what interfaces are for.

    python Abstract_Base_Class_Interfaces_solution.py
"""

from abc import ABC, abstractmethod


#  1.1 - 1.3: a plain base class
class Sensor:
    def measure_distance(self) -> float:
        print("Sensor: I'm the base class.")
        return 0.0


class Radar(Sensor):
    def measure_distance(self) -> float:
        print("Radar: 80.0 m")
        return 80.0


class Camera(Sensor):
    def get_distance(self) -> float:  # 1.3: a colleague picked a different name
        print("Camera: 60.0 m")
        return 60.0


#  1.4: an abstract base class = an interface
class DistanceSensor(ABC):
    @abstractmethod
    def measure_distance(self) -> float:
        """Distance to the vehicle ahead in m."""


class Lidar(DistanceSensor):
    def measure_distance(self) -> float:
        print("Lidar: 75.0 m")
        return 75.0


class Ultrasonic(DistanceSensor):
    def get_distance(self) -> float:  # 1.4: the same mistake as in Camera
        print("Ultrasonic: 2.0 m")
        return 2.0


#  1.5: no base class at all
class V2XReceiver:
    """Vehicle-to-X: the vehicle ahead sends its position over the air."""

    def measure_distance(self) -> float:
        print("V2X: 70.0 m")
        return 70.0


#  High-level code: depends only on the interface
def check_distance(sensor: DistanceSensor) -> None:
    distance = sensor.measure_distance()
    print("  -> BRAKE!" if distance < 30.0 else "  -> OK")


if __name__ == "__main__":
    print("\n1.2  check_distance(Radar())")
    check_distance(Radar())

    print("\n1.3  check_distance(Camera())")
    check_distance(Camera())

    print("\n1.4  check_distance(Lidar())  and  check_distance(Ultrasonic())")
    check_distance(Lidar())
    try:
        check_distance(Ultrasonic())
    except TypeError as error:
        print(f"TypeError: {error}")
    try:
        DistanceSensor()
    except TypeError as error:
        print(f"TypeError: {error}")

    print("\n1.5  check_distance(V2XReceiver())")
    check_distance(V2XReceiver())
