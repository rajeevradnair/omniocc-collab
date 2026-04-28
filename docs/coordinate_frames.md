# Coordinate Frame Convention

This project uses a simplified autonomous-driving coordinate convention.

## Ego Frame

The ego frame is centered on the main vehicle.

For this project:

| Axis | Meaning |
|---|---|
| x | forward from the ego vehicle |
| y | left/right from the ego vehicle |
| z | height above the ground |

Positive x means forward.

Positive y means left.

Positive z means upward.

## Sensor Frame

The sensor frame is centered on a specific sensor, such as LiDAR or camera.

A point in the sensor frame tells us where the point is relative to that sensor.

To use the point for vehicle-level perception, we transform it into the ego frame.

## World Frame

The world frame is a shared scene-level coordinate system.

A point in the world frame tells us where the point is in the larger driving scene, not just relative to one vehicle.

## Why Frames Matter

The same physical object can have different coordinates in different frames.

For example, a cone may be:

- 3 meters in front of the LiDAR sensor
- 4 meters in front of the ego vehicle
- 105 meters east and 40 meters north in the world frame

The object did not move. Only the reference frame changed.

## Main Transform Chain

For early project work:

```text
sensor point → ego point → world point