import pytest

import boggle_solver

size = 4
grid = boggle_solver.make_grid(size=size)


def test_grid_rows(grid=grid):
    """Test that the grid has a number of rows equal to `size`"""

    assert len(grid) == size


def test_grid_cols(grid=grid):
    """Test each row has length == `size`"""

    result = list(set([len(row) == size for row in grid]))

    assert len(result) == 1 and result[0]


def test_search_grid():
    """Test that the search of a grid point is exhaustive by finding all possible
    valid sequences. A valid sequence is one that visits all possible neighbouring
    coordinates and doesn't visit any coordinate twice."""

    grid = [["t", "o"], ["w", "l"]]

    boggle_solver.search_grid(grid, 0, 0)
