"""
Week 1 Day 2: Plot simple coordinate frames.

This script creates a 2D top-down plot showing:
- the ego vehicle at the origin
- the LiDAR sensor 1 meter ahead
- the observed point
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt


def main() -> None:
    # Create output directory if it does not exist.
    output_dir = Path("assets/diagrams")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Ego vehicle center in ego frame.
    ego_x, ego_y = 0.0, 0.0

    # LiDAR location in ego frame.
    lidar_x, lidar_y = 1.0, 0.0

    # Point location in sensor frame.
    point_sensor_x, point_sensor_y = 4.0, 1.0

    # Convert point into ego frame by adding LiDAR location.
    point_ego_x = lidar_x + point_sensor_x
    point_ego_y = lidar_y + point_sensor_y

    # Create plot.
    plt.figure(figsize=(7, 7))

    # Plot ego vehicle center.
    plt.scatter(ego_x, ego_y, marker="s", s=120, label="Ego vehicle center")

    # Plot LiDAR sensor.
    plt.scatter(lidar_x, lidar_y, marker="^", s=120, label="LiDAR sensor")

    # Plot observed point.
    plt.scatter(point_ego_x, point_ego_y, marker="o", s=120, label="Observed point in ego frame")

    # Draw line from LiDAR to point.
    plt.plot([lidar_x, point_ego_x], [lidar_y, point_ego_y], linestyle="--", label="LiDAR observation")

    # Draw ego forward direction.
    plt.arrow(0, 0, 2, 0, head_width=0.2, length_includes_head=True)
    plt.text(2.2, 0, "+x forward")

    # Draw ego left direction.
    plt.arrow(0, 0, 0, 2, head_width=0.2, length_includes_head=True)
    plt.text(0.1, 2.2, "+y left")

    plt.title("Week 1 Day 2: Sensor Frame to Ego Frame")
    plt.xlabel("x: forward/backward meters")
    plt.ylabel("y: left/right meters")
    plt.grid(True)
    plt.axis("equal")
    plt.legend()

    output_path = output_dir / "week01_day02_sensor_to_ego.png"
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()

    print(f"Saved diagram to: {output_path}")


if __name__ == "__main__":
    main()