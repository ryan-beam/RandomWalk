import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def random_walk_3d(n_steps=1000):
    """Generate a 3D random walk."""
    steps = np.random.choice([-1, 1], size=(n_steps, 3))  # Random ±1 in x,y,z
    path = np.cumsum(steps, axis=0)                        # Convert steps to positions
    return np.vstack([[0, 0, 0], path])                    # Prepend origin

def animate_walk(path, interval=10):
    """Animate the 3D random walk."""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Set axis limits based on full path
    margin = 5
    ax.set_xlim(path[:, 0].min() - margin, path[:, 0].max() + margin)
    ax.set_ylim(path[:, 1].min() - margin, path[:, 1].max() + margin)
    ax.set_zlim(path[:, 2].min() - margin, path[:, 2].max() + margin)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    colors = np.linspace(0, 1, len(path))  # Gradient: 0=start, 1=end
    line_segments = []
    start_marker = ax.scatter(*path[0], color='green', s=100, label='Start', zorder=5)
    end_marker = ax.scatter([], [], [], color='red', s=100, label='End', zorder=5)
    ax.legend()

    def update(frame):
        # Add new segment
        if frame > 0:
            seg, = ax.plot(path[frame-1:frame+1, 0], path[frame-1:frame+1, 1],
                          path[frame-1:frame+1, 2], color=plt.cm.viridis(colors[frame]), alpha=0.7)
            line_segments.append(seg)
        # Update end marker position
        end_marker._offsets3d = ([path[frame, 0]], [path[frame, 1]], [path[frame, 2]])
        ax.set_title(f'3D Random Walk (step {frame}/{len(path)-1})')
        return line_segments + [end_marker]

    anim = FuncAnimation(fig, update, frames=len(path), interval=interval, blit=False, repeat=False)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    path = random_walk_3d(n_steps=500)  # Fewer steps for smoother animation
    animate_walk(path, interval=20)     # 20ms between frames