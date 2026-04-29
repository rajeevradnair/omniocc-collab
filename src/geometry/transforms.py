"""
Geometry transforms for OmniOcc-Collab.

Week 1 Day 3 focuses on the standard rigid-body transform:

    p_new = R @ p + t

where:
- p is a 3D point
- R is a 3x3 rotation matrix
- t is a 3D translation vector

"""

from __future__ import annotations

import math

import numpy as np


def yaw_rotation_matrix(yaw_radians: float) -> np.ndarray:
    """
    Create a 3D rotation matrix for yaw rotation around the z-axis.

    In this project:
    - x means forward
    - y means left/right
    - z means up

    A positive yaw angle rotates x toward y.

    Parameters
    ----------
    yaw_radians:
        Rotation angle in radians.

    Returns
    -------
    np.ndarray
        A 3x3 rotation matrix.

    Example
    -------
    yaw = 90 degrees = pi / 2 radians

    A point [1, 0, 0] becomes approximately [0, 1, 0].
    """
    cos_theta = math.cos(yaw_radians)
    sin_theta = math.sin(yaw_radians)

    rotation = np.array(
        [
            [cos_theta, -sin_theta, 0.0],
            [sin_theta, cos_theta, 0.0],
            [0.0, 0.0, 1.0],
        ],
        dtype=float,
    )

    return rotation


def transform_point(
    point: np.ndarray,
    rotation: np.ndarray,
    translation: np.ndarray,
) -> np.ndarray:
    """
    Transform one 3D point using rotation and translation.

    Formula:
        new_point = rotation @ point + translation

    Parameters
    ----------
    point:
        A NumPy array with shape (3,).

    rotation:
        A NumPy array with shape (3, 3).

    translation:
        A NumPy array with shape (3,).

    Returns
    -------
    np.ndarray
        Transformed point with shape (3,).
    """
    point = np.asarray(point, dtype=float)
    rotation = np.asarray(rotation, dtype=float)
    translation = np.asarray(translation, dtype=float)

    if point.shape != (3,):
        raise ValueError(f"point must have shape (3,), got {point.shape}")

    if rotation.shape != (3, 3):
        raise ValueError(f"rotation must have shape (3, 3), got {rotation.shape}")

    if translation.shape != (3,):
        raise ValueError(f"translation must have shape (3,), got {translation.shape}")

    return rotation @ point + translation


def transform_points(
    points: np.ndarray,
    rotation: np.ndarray,
    translation: np.ndarray,
) -> np.ndarray:
    """
    Transform many 3D points using the same rotation and translation.

    Formula for each point:
        new_point = rotation @ point + translation

    Parameters
    ----------
    points:
        NumPy array with shape (N, 3).

    rotation:
        NumPy array with shape (3, 3).

    translation:
        NumPy array with shape (3,).

    Returns
    -------
    np.ndarray
        Transformed points with shape (N, 3).

    Notes
    -----
    For many points, we use:

        points @ rotation.T + translation

    This is equivalent to applying:

        rotation @ point + translation

    to each individual row point.
    """
    points = np.asarray(points, dtype=float)
    rotation = np.asarray(rotation, dtype=float)
    translation = np.asarray(translation, dtype=float)

    if points.ndim != 2 or points.shape[1] != 3:
        raise ValueError(f"points must have shape (N, 3), got {points.shape}")

    if rotation.shape != (3, 3):
        raise ValueError(f"rotation must have shape (3, 3), got {rotation.shape}")

    if translation.shape != (3,):
        raise ValueError(f"translation must have shape (3,), got {translation.shape}")

    return points @ rotation.T + translation