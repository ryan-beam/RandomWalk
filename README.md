# Random Walk Visualization

Python scripts that simulate and visualize random walks — mathematical models where a particle takes successive random steps in space. Includes both 2D and 3D implementations.

## What is a Random Walk?

A random walk is a stochastic process where an object moves in random directions at each step. These implementations use discrete random walks where the particle moves ±1 unit in each dimension at every step.

## Files

- `randomWalk2D.py` - 2D random walk visualization with grid overlay
- `randomWalk3D.py` - 3D random walk visualization with interactive rotation

## Features

- Generates random walks with configurable number of steps
- Animated visualizations with color gradients showing progression over time
- Marks start (green) and end (red) points
- **2D version**: Grid overlay and equal aspect ratio for accurate visualization
- **3D version**: Interactive 3D plot you can rotate and zoom

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Installation

```bash
pip install numpy matplotlib
```

## Usage

Run either script directly:

```bash
# 2D random walk
python randomWalk2D.py

# 3D random walk
python randomWalk3D.py
```

Or import and customize in your own code:

```python
# 2D example
from randomWalk2D import random_walk_2d, animate_walk
path = random_walk_2d(n_steps=500)
animate_walk(path, interval=20)

# 3D example
from randomWalk3D import random_walk_3d, animate_walk
path = random_walk_3d(n_steps=500)
animate_walk(path, interval=20)
```

## Example Output

The visualizations display animated plots showing the particle's wandering path through space, colored from purple (start) to yellow (end) using the viridis colormap.

## License

MIT
