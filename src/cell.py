# src.cell 

"""
This module defines the Cell class
True: alive, False: dead
Reproduction: 3 neighbors
Neighbors: the 8 cells surrounding a cell
"""

class Cell:
    """ A cell is a basic unit of this program.
        Defines a cell on the grid"""

    __slots__ = ("_alive", "_next")

    def __init__(self, alive: bool = False):
        """
        Initializes a Cell instance.

        Args:
            alive (bool): Indicates whether the cell is alive or not. Defaults to False.
        """
        self._alive = alive
        self._next = alive

    @property
    def alive(self) -> bool:
        """Returns the alive status of the cell."""
        return self._alive

    def set_alive(self, value: bool):
        """Sets the alive status of the cell."""
        self._alive = bool(value)

    def compute_nextstate(self, live_neighbors: int):
        """
        Apply Conway's rule, save to next state (not applied).

        Args:
            live_neighbors (int): The number of live neighboring cells.
        """
        if self.alive:
            self._next = live_neighbors in (2, 3) # True if 2 or 3 neighbors, else False

        else:
            self._next = live_neighbors == 3 # True if exactly 3 neighbors, else False

    def commit(self) -> None:
        """Commit the next state to the current state."""
        self._alive = self._next





        