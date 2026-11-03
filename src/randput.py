# src.randput

import random as rd

def random_put(grid, alive_prob=0.5):
    """
    Populating the grid with random alive cells based on a specified probability.
    """

    for row in grid.grid:
        for cell in row:
            cell.set_alive(rd.random() < alive_prob)

    