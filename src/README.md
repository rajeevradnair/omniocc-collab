# OmniOcc-Collab

OmniOcc-Collab is a beginner-friendly but serious portfolio project for building a collaborative real-time semantic 3D occupancy system.

The goal is to predict which parts of 3D space around an ego vehicle are occupied and what semantic class occupies that space, such as car, pedestrian, road, sidewalk, or background.

The project starts from first principles:
- geometry
- coordinate frames
- projection
- voxel grids
- sparse LiDAR-based occupancy
- semantic occupancy prediction
- temporal fusion
- collaborative multi-agent fusion
- robustness to delay, dropout, and pose noise
- SageMaker-based training and inference
- monitoring and portfolio-ready deployment

## Core Problem

A camera image is 2D, but a vehicle moves in 3D space.

A self-driving system needs to know not only what is visible in an image, but also which physical regions around the car are occupied, empty, unknown, or semantically meaningful.

For example:
- Is there a pedestrian behind a parked truck?
- Is the space in front of the car occupied?
- Is the object a car, sidewalk, curb, cyclist, or road region?
- Can a neighboring vehicle help reveal something the ego vehicle cannot see?

## What This Project Builds

This project builds a simplified version of a collaborative semantic occupancy system.

The system will eventually support:

1. Ego-only occupancy prediction  
2. Temporal fusion using previous frames  
3. Simulated neighboring-agent observations  
4. Neighbor-to-ego coordinate alignment  
5. Prediction-level fusion  
6. Confidence-weighted fusion  
7. Attention-based fusion  
8. Occlusion-specific evaluation  
9. Delay, dropout, and pose-noise robustness testing  
10. SageMaker training, inference, and monitoring  

## Label Strategy

This project is designed so it does not get blocked by unavailable dense occupancy labels.

It supports three label modes:

| Mode | Description |
|---|---|
| Synthetic labels | Toy scenes created manually for geometry, training, and collaborative fusion |
| Sparse LiDAR occupancy labels | A voxel is marked occupied if one or more LiDAR points fall inside it |
| Optional dense occupancy labels | OpenOccupancy or Occ3D-style labels if available and successfully prepared |

The project will be honest about the difference between sparse occupancy and true dense occupancy.

## Beginner Definitions

### Pixel

A pixel is a small square in a 2D image.

An image may have shape:

```text
Height x Width x Channels