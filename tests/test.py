from pathlib import Path

import numpy as np

from Library import case_10


def test_case_10_mapping_matches_assigned_parameters():
    x = np.array([[-3.0, 0.0, 3.0], [-3.0, 0.0, 3.0]])
    y = np.array([[-1.5, -1.5, -1.5], [0.75, 0.75, 0.75]])

    x_deformed, y_deformed = case_10(x, y)

    expected_x = x + 0.15 * np.sin(2 * np.pi * y / 3) * np.exp(-x / 3)
    assert np.allclose(x_deformed, expected_x)
    assert np.allclose(y_deformed, y)


def test_case_10_is_surface_confined_x_displacement():
    x = np.array([-3.0, 0.0, 3.0])
    y = np.array([0.75, 0.75, 0.75])

    x_deformed, y_deformed = case_10(x, y)
    displacement = x_deformed - x

    assert displacement[0] > displacement[1] > displacement[2]
    assert np.allclose(y_deformed, y)


def test_grid_output_exists():
    assert Path("grid.png").is_file()
