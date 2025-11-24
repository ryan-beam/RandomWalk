# 3D Random Walk Visualization

A Python script that simulates and visualizes a 3D random walk  a mathematical model where a particle takes successive random steps in three-dimensional space.

## What is a Random Walk?

A random walk is a stochastic process where an object moves in random directions at each step. This implementation uses a discrete random walk where the particle moves ±1 unit in each dimension (X, Y, Z) at every step.

## Features

- Generates a 3D random walk with configurable number of steps
- Visualizes the path with a color gradient showing progression over time
- Marks start (green) and end (red) points
- Interactive 3D plot you can rotate and zoom

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Installation

```bash
pip install numpy matplotlib
```

## Usage

Run the script directly:

```bash
python randomWalk3D.py
```

Or import and customize in your own code:

```python
from randomWalk3D import random_walk_3d, plot_walk

# Generate a walk with 5000 steps
path = random_walk_3d(n_steps=5000)
plot_walk(path)
```

## Example Output

The visualization displays an interactive 3D plot showing the particle's wandering path through space, colored from purple (start) to yellow (end) using the viridis colormap.

## License

MIT
