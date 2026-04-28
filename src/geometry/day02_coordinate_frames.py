"""
Week 1 Day 2: Coordinate Frame Demo

This script shows how the same physical point can have different coordinates
depending on the coordinate frame.

A simple example:

1. A LiDAR sensor observes a point.
2. The LiDAR sensor is mounted 1 meter in front of the ego vehicle center.
3. We transform the point from sensor frame into ego frame.
4. Then we transform the ego-frame point into a simple world frame.

This is not yet full calibration math.
"""

from __future__ import annotations

import numpy as np


def translate_point(point: np.ndarray, translation: np.ndarray) -> np.ndarray:
    """
    Move a 3D point by a translation vector.

    Parameters
    ----------
    point:
        A NumPy array with shape (3,).
        Example: [4.0, 1.0, 0.0]

    translation:
        A NumPy array with shape (3,).
        Example: [1.0, 0.0, 0.0]

    Returns
    -------
    np.ndarray
        The translated point.

    Example
    -------
    point = [4, 1, 0]
    translation = [1, 0, 0]

    result = [5, 1, 0]
    """
    return point + translation


def main() -> None:
    # ------------------------------------------------------------
    # 1. A point observed by the LiDAR sensor
    # ------------------------------------------------------------
    # Meaning:
    # x = 4 meters forward from the LiDAR
    # y = 1 meter left from the LiDAR
    # z = 0 meters high relative to the LiDAR
    point_in_sensor_frame = np.array([4.0, 1.0, 0.0])

    # ------------------------------------------------------------
    # 2. Sensor location relative to ego vehicle center
    # ------------------------------------------------------------
    # Meaning:
    # The LiDAR is mounted 1 meter in front of the ego vehicle center.
    sensor_to_ego_translation = np.array([1.0, 0.0, 0.0])

    # ------------------------------------------------------------
    # 3. Transform sensor-frame point into ego frame
    # ------------------------------------------------------------
    point_in_ego_frame = translate_point(
        point=point_in_sensor_frame,
        translation=sensor_to_ego_translation,
    )

    # ------------------------------------------------------------
    # 4. Ego vehicle location in the world frame
    # ------------------------------------------------------------
    # Meaning:
    # The ego vehicle center is located at world coordinate [100, 50, 0].
    ego_to_world_translation = np.array([100.0, 50.0, 0.0])

    # ------------------------------------------------------------
    # 5. Transform ego-frame point into world frame
    # ------------------------------------------------------------
    point_in_world_frame = translate_point(
        point=point_in_ego_frame,
        translation=ego_to_world_translation,
    )

    # ------------------------------------------------------------
    # 6. Print results
    # ------------------------------------------------------------
    print("Coordinate Frame Demo")
    print("---------------------")
    print(f"Point in sensor frame: {point_in_sensor_frame}")
    print(f"Sensor-to-ego translation: {sensor_to_ego_translation}")
    print(f"Point in ego frame: {point_in_ego_frame}")
    print(f"Ego-to-world translation: {ego_to_world_translation}")
    print(f"Point in world frame: {point_in_world_frame}")


if __name__ == "__main__":
    main()