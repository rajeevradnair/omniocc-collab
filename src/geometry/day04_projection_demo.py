"""
Week 1 Day 4 Demo: Project 3D camera points to 2D pixels.

This script uses a simple pinhole camera model.

Camera frame convention:
- X = right
- Y = down
- Z = forward
"""

from __future__ import annotations

import numpy as np

from src.geometry.projection import project_point_to_pixel, project_points_to_pixels


def main() -> None:
    # ------------------------------------------------------------
    # 1. Define fake camera intrinsics.
    # ------------------------------------------------------------
    image_width = 1280
    image_height = 720

    fx = 800.0
    fy = 800.0
    cx = image_width / 2.0
    cy = image_height / 2.0

    print("Camera intrinsics")
    print("-----------------")
    print(f"image_width: {image_width}")
    print(f"image_height: {image_height}")
    print(f"fx: {fx}")
    print(f"fy: {fy}")
    print(f"cx: {cx}")
    print(f"cy: {cy}")

    # ------------------------------------------------------------
    # 2. Project one point.
    # ------------------------------------------------------------
    point_camera = np.array([2.0, 1.0, 10.0])

    pixel = project_point_to_pixel(
        point_camera=point_camera,
        fx=fx,
        fy=fy,
        cx=cx,
        cy=cy,
    )

    print()
    print("Single point projection")
    print("-----------------------")
    print(f"3D camera point [X, Y, Z]: {point_camera}")
    print(f"Projected pixel [u, v]: {pixel}")

    # ------------------------------------------------------------
    # 3. Project multiple points.
    # ------------------------------------------------------------
    points_camera = np.array(
        [
            [0.0, 0.0, 10.0],   # image center
            [2.0, 0.0, 10.0],   # right
            [-2.0, 0.0, 10.0],  # left
            [0.0, 1.0, 10.0],   # down
            [0.0, -1.0, 10.0],  # up
            [2.0, 1.0, 5.0],    # closer, appears farther from center
            [2.0, 1.0, 20.0],   # farther, appears closer to center
            [1.0, 1.0, -3.0],   # invalid: behind camera
        ]
    )

    pixels, valid_mask = project_points_to_pixels(
        points_camera=points_camera,
        fx=fx,
        fy=fy,
        cx=cx,
        cy=cy,
    )

    print()
    print("Batch projection")
    print("----------------")
    print(f"Valid mask: {valid_mask}")

    valid_points = points_camera[valid_mask]

    for point, projected_pixel in zip(valid_points, pixels):
        print(f"3D point {point} -> pixel {projected_pixel}")


if __name__ == "__main__":
    main()