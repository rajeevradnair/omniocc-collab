# Week 1 Day 2 — Coordinate Frame Diagram

## Toy Example

A LiDAR sensor sees a point at:

```text
Sensor frame point = [4, 1, 0]
Sensor to ego translation = [1, 0, 0]
Ego frame point = [5, 1, 0]
Ego to world translation = [100, 50, 0]
World frame point = [105, 51, 0]

Sensor Frame
[4, 1, 0]
    |
    | add sensor_to_ego = [1, 0, 0]
    v
Ego Frame
[5, 1, 0]
    |
    | add ego_to_world = [100, 50, 0]
    v
World Frame
[105, 51, 0]