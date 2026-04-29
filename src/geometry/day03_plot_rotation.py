"""
Week 1 Day 3: Plot rotation + translation.

This creates a top-down visualization of:
- original sensor-frame point
- rotated point
- final translated ego-frame point
"""

from __future__ import annotations

from pathlib import Path
import math

import matplotlib.pyplot as plt
import numpy as np

from src.geometry.transforms import yaw_rotation_matrix


def main() -> None:
    output_dir = Path("assets/diagrams")
    output_dir.mkdir(parents=True, exist_ok=True)

    point_sensor = np.array([2.0, 0.0, 0.0])
    rotation = yaw_rotation_matrix(math.radians(90.0))
    translation = np.array([1.0, 0.0, 0.0])

    point_rotated = rotation @ point_sensor
    point_ego = point_rotated + translation

    plt.figure(figsize=(7, 7))

    # Plot origin
    plt.scatter(0, 0, marker="s", s=120, label="Origin")

    # Plot original point
    plt.scatter(
        point_sensor[0],
        point_sensor[1],
        marker="o",
        s=120,
        label="Original sensor point [2, 0]",
    )

    # Plot rotated point
    plt.scatter(
        point_rotated[0],
        point_rotated[1],
        marker="^",
        s=120,
        label="After rotation [0, 2]",
    )

    # Plot final point
    plt.scatter(
        point_ego[0],
        point_ego[1],
        marker="*",
        s=180,
        label="After rotation + translation [1, 2]",
    )

    # Draw arrows
    plt.arrow(0, 0, point_sensor[0], point_sensor[1], head_width=0.12, length_includes_head=True)
    plt.arrow(0, 0, point_rotated[0], point_rotated[1], head_width=0.12, length_includes_head=True)
    plt.arrow(point_rotated[0], point_rotated[1], translation[0], translation[1], head_width=0.12, length_includes_head=True)

    plt.title("Rotation + Translation")
    plt.xlabel("x: forward meters")
    plt.ylabel("y: left meters")
    plt.grid(True)
    plt.axis("equal")
    plt.legend()

    output_path = output_dir / "week01_day03_rotation_translation.png"
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()

    print(f"Saved plot to: {output_path}")


if __name__ == "__main__":
    main()