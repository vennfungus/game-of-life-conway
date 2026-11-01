"""
Controlling and Visualising the Game of Life using a grid of cells.
This module defines the Grid class, which represents a 2D grid of cells for Conway's Game of Life. Each cell can be alive or dead, and the grid can be configured to be toroidal (wrapping around edges) or not.
"""

from matplotlib import animation
import numpy as np
from src.cell import Cell
from src.grid import Grid
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Game:
    """ The Game class manages the grid and the rules of Conway's Game of Life.
        It provides methods to step through generations and visualize the grid."""
    
    def __init__(self, grid: Grid, interval_ms: int = 100):
        self.grid = grid
        self.interval_ms = interval_ms  # Interval in milliseconds for visualization updates
        self.gen = 0  # Generation counter

    def step(self):
        """Advance the game by one generation."""
        self.grid.step()
        self.gen += 1


    def run_console(self, generations: int):
        """Run the game in console mode for a specified number of generations."""
        for _ in range(generations):
            self._display()
            self.step()

    def _display(self):
        """Display the current state of the grid in the console."""
        print(f"Generation: {self.gen}")
        for row in self.grid.grid:
            print(' '.join(['█' if cell.alive else ' ' for cell in row]))
        print("\n" + "-" * (self.grid.cols * 2))

    def run_visual(self, frames: int = 200) -> animation.FuncAnimation:
        """Run the game with a visual representation using matplotlib."""

        fig, ax = plt.subplots()
        img = ax.imshow(self.grid.to_numpy(), cmap='binary',
                         interpolation='nearest', vmin=0, vmax=1)
        ax.set_title(f"Game of Life | Generation: {self.gen}")
        ax.axis('off')  # Hide axes for better visualization
        
        def update(_): # set "_" as the argument to ignore the frame number
            self.step()
            img.set_array(self.grid.to_numpy())
            ax.set_title(f"Game of Life | Generation: {self.gen}")
            return [img]

        ani = animation.FuncAnimation(
            fig, update, frames, interval=self.interval_ms, 
                blit=False
            )
        plt.show()

        return ani


