# src.grid

"""
This module defines the Grid class, which represents a grid of cells for Conway's Game of Life.
The grid is a 2D array of Cell objects, where each cell can be alive or dead.
"""

from src.cell import Cell
import numpy as np

class Grid:
    """ A grid is a collection of cells arranged in a 2D array.
        It represents the environment for Conway's Game of Life."""

    def __init__(self, rows: int = 25, cols: int = 25, toroidal: bool = True):
        """
        Initializes a Grid instance.

        Args:
            rows (int): The number of rows in the grid. Defaults to 25.
            cols (int): The number of columns in the grid. Defaults to 25.
            toroidal (bool): Whether the grid is toroidal (wraps around edges). Defaults to True.
        """
        self.rows = rows
        self.cols = cols
        self.toroidal = toroidal
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]

    #----Accessors----#
    def cell(self, a: int, b: int) -> Cell:
        """Returns the cell at position (a, b)."""
        return self.grid[a][b]

    def is_alive(self, a: int, b: int) -> bool:
        """Returns True if the cell at (a, b) is alive, else False."""
        return self.grid[a][b].alive

    def set_alive(self, a: int, b: int, value: bool):
        """Sets the alive status of the cell at (a, b)."""
        self.grid[a][b].set_alive(value)

    #----Neighbor Counting----#
    def neighbors_coords(self, a: int, b: int) -> list[tuple[int, int]]: #type:ignore
        """
        Returns the coordinates of the 8 neighboring cells of the cell at (a, b).
        If the grid is toroidal, neighbors wrap around the edges.

        Args:
            a (int): The row index of the cell.
            b (int): The column index of the cell.
        Returns:
            list[tuple[int, int]]: A list of tuples representing the coordinates of neighboring cells
        """

        for da in (-1, 0, 1): # Browse the rows
            for db in (-1, 0, 1): # Browse the columns
                if da == 0 and db == 0: # Skip the cell itself
                    continue 
                na, nb = a + da, b + db 
                if self.toroidal:
                    na %= self.rows
                    nb %= self.cols
                elif not (0 <= na < self.rows and 0 <= nb < self.cols):
                    continue
                yield (na, nb)

    def live_neighbors(self, a: int, b: int) -> int:
        """
        Counts the number of live neighbors for the cell at (a, b).

        Args:
            a (int): The row index of the cell.
            b (int): The column index of the cell.
        Returns:
            int: The number of live neighboring cells.
        """

        return sum(1 for na, nb in self.neighbors_coords(a, b) if self.is_alive(na, nb))

    #----Life circle----#
    def step(self):
        """Computes and commits the next state for all cells in the grid based on their neighbors."""
        for a in range(self.rows):
            for b in range(self.cols):
                live_neighbors = self.live_neighbors(a, b)
                self.grid[a][b].compute_nextstate(live_neighbors)

        # commit simultaneously
        for a in range(self.rows):
            for b in range(self.cols):
                self.grid[a][b].commit()

    #----Utility Methods----#
    def to_numpy(self):
        """Converts the grid to a NumPy array representation."""
        return np.array(
            [[ 1 if cell.alive else 0 for cell in row] 
             for row in self.grid], dtype=np.int8)

    def live_countor(self) -> int:
        """Counts the total number of live cells in the grid."""
        return sum(cell.alive for row in self.grid for cell in row)

    #----Initial patterns----#
    @classmethod
    def random(cls, rows: int, cols: int, density: float = 0.5,
               toroidal: bool = True, seed: int | None = None) -> "Grid":
        """
        Creates a grid with random alive cells based on the specified density.

        Args:
            rows (int): The number of rows in the grid.
            cols (int): The number of columns in the grid.
            density (float): The probability of a cell being alive. Defaults to 0.5.
            toroidal (bool): Whether the grid is toroidal. Defaults to True.
            seed (int | None): Seed for the random number generator. Defaults to None.
        Returns:
            Grid: A new Grid instance with randomly initialized cells.
        """
        rng = np.random.default_rng(seed)
        g = cls(rows, cols, toroidal)

        for a in range(rows):
            for b in range(cols):
                g.set_alive(a, b, rng.random() < density)

        return g

    def place(self, pattern: list[list[int]], top_left: tuple[int, int] = (0, 0)):
        """
        Places a predefined pattern of alive cells onto the grid at the specified top-left position.

        Args:
            pattern (list[list[int]]): A 2D list representing the pattern to place (1 for alive, 0 for dead).
            top_left (tuple[int, int]): The (row, column) coordinates of the top-left corner where the pattern will be placed.
        """
        rows, cols = len(pattern), len(pattern[0])
        start_row, start_col = top_left

        for i in range(rows):
            for j in range(cols):
                if 0 <= start_row + i < self.rows and 0 <= start_col + j < self.cols:
                    self.set_alive(start_row + i, start_col + j, bool(pattern[i][j]))


    
    

