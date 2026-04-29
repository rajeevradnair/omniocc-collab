"""
Week 1 Day 3 Demo: Rotation + Translation

This script demonstrates:

    p_new = R @ p + t

We use a toy example:
- A point is 2 meters forward in the sensor frame.
- The sensor is rotated 90 degrees around z.
- The sensor is translated 1 meter forward from the ego vehicle center.
"""

from __future__ import annotations

import math

import numpy as np

from src.geometry.transforms import transform_point, transform_points, yaw_rotation_matrix


def main() -> None:
    # ------------------------------------------------------------
    # 1. Define one point in the sensor frame.
    # ------------------------------------------------------------
    point_sensor = np.array([2.0, 0.0, 0.0])

    # ------------------------------------------------------------
    # 2. Define a 90-degree yaw rotation.
    # ------------------------------------------------------------
    yaw_degrees = 90.0
    yaw_radians = math.radians(yaw_degrees)

    rotation_sensor_to_ego = yaw_rotation_matrix(yaw_radians)

    # ------------------------------------------------------------
    # 3. Define translation from sensor origin to ego origin.
    # ------------------------------------------------------------
    translation_sensor_to_ego = np.array([1.0, 0.0, 0.0])

    # ------------------------------------------------------------
    # 4. Transform the point.
    # ------------------------------------------------------------
    point_ego = transform_point(
        point=point_sensor,
        rotation=rotation_sensor_to_ego,
        translation=translation_sensor_to_ego,
    )

    print("Single Point Transform")
    print("----------------------")
    print(f"Point in sensor frame: {point_sensor}")
    print(f"Yaw rotation degrees: {yaw_degrees}")
    print("Rotation matrix:")
    print(rotation_sensor_to_ego)
    print(f"Translation vector: {translation_sensor_to_ego}")
    print(f"Point in ego frame: {point_ego}")

    # ------------------------------------------------------------
    # 5. Transform multiple points.
    # ------------------------------------------------------------
    points_sensor = np.array(
        [
            [2.0, 0.0, 0.0],
            [4.0, 0.0, 0.0],
            [2.0, 1.0, 0.0],
            [2.0, -1.0, 0.0],
        ]
    )

    points_ego = transform_points(
        points=points_sensor,
        rotation=rotation_sensor_to_ego,
        translation=translation_sensor_to_ego,
    )

    print()
    print("Batch Point Transform")
    print("---------------------")
    for src, dst in zip(points_sensor, points_ego):
        print(f"sensor {src} -> ego {dst}")


if __name__ == "__main__":
    main()