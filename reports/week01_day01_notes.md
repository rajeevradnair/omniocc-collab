# Week 1 Day 1 Notes

A camera image is 2D, but autonomous driving decisions happen in 3D physical space.

A pixel is a small square in an image.

A voxel is a small cube in 3D space.

Occupancy means whether a region of space is empty or filled.

Semantic occupancy means predicting both occupancy and class label.

A self-driving car cannot rely only on a flat picture. It needs to know which parts of the real world around it are free, occupied, or unknown.

To do that, we divide the world into small 3D cubes called voxels.

Each voxel can be labeled as empty, occupied, or occupied by a class such as car, pedestrian, road, or sidewalk.

## Why this matters

If the car knows which 3D regions are occupied, it can plan safer motion.

If another nearby vehicle can see something the ego vehicle cannot see, collaborative perception may help recover hidden objects.