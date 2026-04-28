# Week 1 Day 1 — Glossary

## Pixel

A pixel is a small square in a 2D image. It stores visual information such as color or brightness.

## Voxel

A voxel is a small cube in 3D space. It represents a physical region of the world.

## Occupancy

Occupancy tells whether a voxel is empty or filled by something.

## Semantic Occupancy

Semantic occupancy tells both whether a voxel is occupied and what class occupies it.

Examples:
- car
- pedestrian
- road
- sidewalk
- cyclist
- background

## Ego Vehicle

The ego vehicle is the main vehicle whose coordinate frame and perception output we care about.

## Neighbor Agent

A neighbor agent is another vehicle or sensor source that can share information with the ego vehicle.

## Why 2D Images Are Not Enough

A 2D image shows what is visible from one camera view, but it does not directly describe the 3D physical space around the car.

A vehicle needs 3D understanding because driving decisions depend on distance, direction, height, occlusion, and free space.

## Why 3D Occupancy Matters

3D occupancy helps answer:
- Which space is free?
- Which space is occupied?
- What type of object occupies that space?
- Which areas are unknown because they are occluded?
- Can another agent help reveal hidden regions?