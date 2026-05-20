import numpy as np

def plotgrid(map_func, xlim=(-3, 3), ylim=(-3, 3), grid_size=21):
    """
    Plots a regular grid and its deformation by map_func.
    """
    import matplotlib.pyplot as plt

    # Create the original grid
    x = np.linspace(xlim[0], xlim[1], grid_size)
    y = np.linspace(ylim[0], ylim[1], grid_size)
    X, Y = np.meshgrid(x, y)
    # Apply the deformation function
    X_deformed, Y_deformed = map_func(X, Y)
    # Plot
    fig, ax = plt.subplots(figsize=(8, 8))
    # Plot original grid in light grey
    for i in range(grid_size):
        ax.plot(X[i, :], Y[i, :], color='lightgrey', linewidth=1)
        ax.plot(X[:, i], Y[:, i], color='lightgrey', linewidth=1)
    # Plot deformed grid in blue
    for i in range(grid_size):
        ax.plot(X_deformed[i, :], Y_deformed[i, :], color='C0', linewidth=1)
        ax.plot(X_deformed[:, i], Y_deformed[:, i], color='C0', linewidth=1)

    # Draw a_1 and a_2 axes through origin
    ax.axhline(0, color='black', linewidth=1.2)
    ax.axvline(0, color='black', linewidth=1.2)

    # Ticks at integer positions
    x_ticks = range(int(xlim[0]), int(xlim[1]) + 1)
    y_ticks = range(int(ylim[0]), int(ylim[1]) + 1)
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)
    ax.tick_params(axis='both', direction='inout', length=6)

    # Axis labels
    ax.set_xlabel(r'$a_1$', fontsize=13)
    ax.set_ylabel(r'$a_2$', fontsize=13, rotation=0, labelpad=12)

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect('equal')

    # Move spines to origin instead of box border
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    plt.savefig('grid.png', dpi=150, bbox_inches='tight')
    plt.show()

## Define a deformation function
def case_10(x, y):
    A = 0.15
    L = 3
    h = 3
    return x + A * np.sin(2 * np.pi * y / L) * np.exp(-x / h), y

## how to run
## start a python console
# from Library import plotgrid, case_10

## to generate the plot
# plotgrid(case_10)
