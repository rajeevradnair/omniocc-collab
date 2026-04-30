"""
Week 1 Day 4: Project a synthetic 3D cube onto a 2D image.

This demonstrates how 3D object corners become 2D image points.

Camera frame:
- X = right
- Y = down
- Z = forward
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from src.geometry.projection import project_points_to_pixels


def create_cube_corners(
    center: np.ndarray,
    size: float,
) -> np.ndarray:
    """
    Create the 8 corners of a cube.

    Parameters
    ----------
    center:
        Cube center [X, Y, Z] in camera frame.

    size:
        Side length of cube.

    Returns
    -------
    np.ndarray
        Cube corners with shape (8, 3).
    """
    half = size / 2.0

    offsets = np.array(
        [
            [-half, -half, -half],
            [half, -half, -half],
            [half, half, -half],
            [-half, half, -half],
            [-half, -half, half],
            [half, -half, half],
            [half, half, half],
            [-half, half, half],
        ],
        dtype=float,
    )

    return center + offsets


def plot_projected_cube(
    pixels: np.ndarray,
    image_width: int,
    image_height: int,
    output_path: Path,
) -> None:
    """
    Plot projected cube corners and connect cube edges.
    """
    # Cube edge connections between corner indices.
    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4),
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7),
    ]

    plt.figure(figsize=(10, 6))

    # Draw image boundary.
    plt.xlim(0, image_width)
    plt.ylim(image_height, 0)

    # Plot cube corners.
    plt.scatter(pixels[:, 0], pixels[:, 1], s=50)

    # Draw cube edges.
    for start_idx, end_idx in edges:
        x_values = [pixels[start_idx, 0], pixels[end_idx, 0]]
        y_values = [pixels[start_idx, 1], pixels[end_idx, 1]]
        plt.plot(x_values, y_values)

    plt.title("Projected 3D Cube on 2D Image Plane")
    plt.xlabel("u pixel coordinate")
    plt.ylabel("v pixel coordinate")
    plt.grid(True)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()


def main() -> None:
    image_width = 1280
    image_height = 720

    fx = 800.0
    fy = 800.0
    cx = image_width / 2.0
    cy = image_height / 2.0

    # Cube center in camera frame.
    # X = 0 means centered horizontally.
    # Y = 0 means centered vertically.
    # Z = 10 means 10 meters in front of the camera.
    cube_center = np.array([0.0, 0.0, 10.0])
    cube_size = 2.0

    cube_corners = create_cube_corners(center=cube_center, size=cube_size)

    pixels, valid_mask = project_points_to_pixels(
        points_camera=cube_corners,
        fx=fx,
        fy=fy,
        cx=cx,
        cy=cy,
    )

    if not valid_mask.all():
        raise RuntimeError("Some cube corners are behind the camera. Move cube farther forward.")

    output_path = Path("assets/diagrams/week01_day04_projected_cube.png")

    plot_projected_cube(
        pixels=pixels,
        image_width=image_width,
        image_height=image_height,
        output_path=output_path,
    )

    print("Cube corners in 3D camera frame:")
    print(cube_corners)
    print()
    print("Projected cube corners in 2D pixels:")
    print(pixels)
    print()
    print(f"Saved projected cube plot to: {output_path}")


if __name__ == "__main__":
    main()