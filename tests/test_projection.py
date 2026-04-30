"""
Tests for projection utilities.
"""

from __future__ import annotations

import numpy as np
import pytest

from src.geometry.projection import project_point_to_pixel, project_points_to_pixels


def test_center_point_projects_to_principal_point() -> None:
    point = np.array([0.0, 0.0, 10.0])

    pixel = project_point_to_pixel(
        point_camera=point,
        fx=800.0,
        fy=800.0,
        cx=640.0,
        cy=360.0,
    )

    expected = np.array([640.0, 360.0])

    np.testing.assert_allclose(pixel, expected)


def test_positive_x_projects_right() -> None:
    point = np.array([2.0, 0.0, 10.0])

    pixel = project_point_to_pixel(
        point_camera=point,
        fx=800.0,
        fy=800.0,
        cx=640.0,
        cy=360.0,
    )

    expected = np.array([800.0, 360.0])

    np.testing.assert_allclose(pixel, expected)


def test_positive_y_projects_down() -> None:
    point = np.array([0.0, 1.0, 10.0])

    pixel = project_point_to_pixel(
        point_camera=point,
        fx=800.0,
        fy=800.0,
        cx=640.0,
        cy=360.0,
    )

    expected = np.array([640.0, 440.0])

    np.testing.assert_allclose(pixel, expected)


def test_point_behind_camera_raises_error() -> None:
    point = np.array([1.0, 1.0, -1.0])

    with pytest.raises(ValueError):
        project_point_to_pixel(
            point_camera=point,
            fx=800.0,
            fy=800.0,
            cx=640.0,
            cy=360.0,
        )


def test_batch_projection_filters_invalid_points() -> None:
    points = np.array(
        [
            [0.0, 0.0, 10.0],
            [2.0, 0.0, 10.0],
            [1.0, 1.0, -3.0],
        ]
    )

    pixels, valid_mask = project_points_to_pixels(
        points_camera=points,
        fx=800.0,
        fy=800.0,
        cx=640.0,
        cy=360.0,
    )

    expected_mask = np.array([True, True, False])
    expected_pixels = np.array(
        [
            [640.0, 360.0],
            [800.0, 360.0],
        ]
    )

    np.testing.assert_array_equal(valid_mask, expected_mask)
    np.testing.assert_allclose(pixels, expected_pixels)