# The Game of Life | Conway
Game of Life is proposed in 1970, by a British mathematician John Horton Conway. The concept is using to visualise chaos concept, butterfly effect, and/or emergence, mainly.

The concept is constructed with just only four simple principles:

```text
1. Any living cell with fewer than two living neighbors dies — as if by underpopulation.
2. Any living cell with two or three living neighbors lives on to the next generation.
3. Any living cell with more than three living neighbors dies — as if by overpopulation.
4. Any dead cell with exactly three living neighbors becomes a living cell — as if by reproduction.
```
All cells update based on these rules, and the grid evolves generation by generation, simultaneously.

## Project Structure
```
game-of-life-conway/
├── main.py          # Class of Game, control live circle and visualise
├── src/
│   ├── cell.py      # Class of Cell: living/dead of cell, rules of change next state
│   └── grid.py      # Class of Grid: handling neighbors, step, place, random, RLE…
├── README.md
└── .gitignore
```

## Installation and Usage

Because of the syntax already used `int | None`, this project requires Python == **3.10** or greater. 
```bash
git clone https://github.com/vennfungus/game-of-life-conway.git
cd game-of-life
```

Since the used `requirements` is popular in Python (am implying numpy and matplotlib), I supposed to not build a `requirements.txt` file. But in the instance which is necessary, run the following command in bash.
```bash
pip install numpy matplotlib
```

## Roadmap in Future
- Allowing create/t.toggle cell while running visualisation, by clicking on screen.
- Export GIF/MP4
- Strengthening with Hashlife
- Randomly create input cells in the begin.
