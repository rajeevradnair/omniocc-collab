"""
Projection utilities for OmniOcc-Collab.

Week 1 Day 4 focuses on pinhole camera projection:

    u = fx * X / Z + cx
    v = fy * Y / Z + cy

where:
- X, Y, Z are camera-frame coordinates
- Z is depth in front of the camera
- fx, fy are focal lengths in pixels
- cx, cy define the image center / principal point
"""

from __future__ import annotations

import numpy as np


def project_point_to_pixel(
    point_camera: np.ndarray,
    fx: float,
    fy: float,
    cx: float,
    cy: float,
    min_depth: float = 1e-6,
) -> np.ndarray:
    """
    Project one 3D camera-frame point into one 2D image pixel.

    Camera coordinate convention for this function:
    - X = right
    - Y = down
    - Z = forward / depth

    Parameters
    ----------
    point_camera:
        NumPy array with shape (3,), representing [X, Y, Z].

    fx:
        Focal length in pixels along image x-axis.

    fy:
        Focal length in pixels along image y-axis.

    cx:
        Principal point x-coordinate, usually image_width / 2.

    cy:
        Principal point y-coordinate, usually image_height / 2.

    min_depth:
        Small positive threshold. Points with Z <= min_depth are invalid.

    Returns
    -------
    np.ndarray
        Pixel coordinate [u, v].

    Raises
    ------
    ValueError
        If the point does not have shape (3,) or is behind the camera.
    """
    point_camera = np.asarray(point_camera, dtype=float)

    if point_camera.shape != (3,):
        raise ValueError(f"point_camera must have shape (3,), got {point_camera.shape}")

    x, y, z = point_camera

    if z <= min_depth:
        raise ValueError(f"Point depth must be positive. Got Z={z}")

    u = fx * (x / z) + cx
    v = fy * (y / z) + cy

    return np.array([u, v], dtype=float)


def project_points_to_pixels(
    points_camera: np.ndarray,
    fx: float,
    fy: float,
    cx: float,
    cy: float,
    min_depth: float = 1e-6,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Project many 3D camera-frame points into 2D image pixels.

    Parameters
    ----------
    points_camera:
        NumPy array with shape (N, 3).

    fx, fy, cx, cy:
        Camera intrinsics.

    min_depth:
        Points with Z <= min_depth are marked invalid.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        pixels:
            NumPy array with shape (M, 2), where M is number of valid points.
        valid_mask:
            Boolean array with shape (N,), True for valid projected points.

    Notes
    -----
    Invalid points behind the camera are filtered out.
    """
    points_camera = np.asarray(points_camera, dtype=float)

    if points_camera.ndim != 2 or points_camera.shape[1] != 3:
        raise ValueError(f"points_camera must have shape (N, 3), got {points_camera.shape}")

    z = points_camera[:, 2]
    valid_mask = z > min_depth

    # Drop the invalid points. Invalid defined as points with z<=min_depth
    valid_points = points_camera[valid_mask] 

    if valid_points.shape[0] == 0:
        return np.empty((0, 2), dtype=float), valid_mask

    x_valid = valid_points[:, 0]
    y_valid = valid_points[:, 1]
    z_valid = valid_points[:, 2]

    u = fx * (x_valid / z_valid) + cx
    v = fy * (y_valid / z_valid) + cy

    pixels = np.stack([u, v], axis=1)

    return pixels, valid_mask