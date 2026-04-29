"""
Tests for geometry transforms.

These tests make sure our beginner transform functions behave correctly.
"""

from __future__ import annotations

import math

import numpy as np

from src.geometry.transforms import transform_point, transform_points, yaw_rotation_matrix


def test_identity_transform_keeps_point_same() -> None:
    point = np.array([2.0, 3.0, 1.0])
    rotation = np.eye(3)
    translation = np.array([0.0, 0.0, 0.0])

    result = transform_point(point, rotation, translation)

    np.testing.assert_allclose(result, point)


def test_translation_only_moves_point() -> None:
    point = np.array([2.0, 3.0, 1.0])
    rotation = np.eye(3)
    translation = np.array([1.0, -1.0, 2.0])

    result = transform_point(point, rotation, translation)

    expected = np.array([3.0, 2.0, 3.0])
    np.testing.assert_allclose(result, expected)


def test_yaw_90_rotates_x_axis_to_y_axis() -> None:
    point = np.array([1.0, 0.0, 0.0])
    rotation = yaw_rotation_matrix(math.radians(90.0))
    translation = np.array([0.0, 0.0, 0.0])

    result = transform_point(point, rotation, translation)

    expected = np.array([0.0, 1.0, 0.0])
    np.testing.assert_allclose(result, expected, atol=1e-7)


def test_rotation_plus_translation() -> None:
    point = np.array([2.0, 0.0, 0.0])
    rotation = yaw_rotation_matrix(math.radians(90.0))
    translation = np.array([1.0, 0.0, 0.0])

    result = transform_point(point, rotation, translation)

    expected = np.array([1.0, 2.0, 0.0])
    np.testing.assert_allclose(result, expected, atol=1e-7)


def test_transform_multiple_points() -> None:
    points = np.array(
        [
            [1.0, 0.0, 0.0],
            [2.0, 0.0, 0.0],
            [3.0, 0.0, 0.0],
        ]
    )

    rotation = np.eye(3)
    translation = np.array([10.0, 0.0, 0.0])

    result = transform_points(points, rotation, translation)

    expected = np.array(
        [
            [11.0, 0.0, 0.0],
            [12.0, 0.0, 0.0],
            [13.0, 0.0, 0.0],
        ]
    )

    np.testing.assert_allclose(result, expected)