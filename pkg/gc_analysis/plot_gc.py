"""
plot_gc.py

This script generates and saves three different visualizations for GC content:
- Histogram of GC content distribution
- Line plot showing GC content for each sequence
- Scatter plot for GC content distribution

Functions:
- histogram(gc_contents): Plots and saves a histogram.
- line(gc_contents): Plots and saves a line chart.
- scatter(gc_contents): Plots and saves a scatter plot.
"""

import matplotlib.pyplot as plt
from pkg.utils import paths  # Import paths for saving plots

def histogram(gc_contents):
    """
    Plot and save a histogram of GC content distribution.

    :param gc_contents: List of GC content percentages.
    """
    plt.figure(figsize=(8, 5))
    plt.hist(gc_contents, bins='auto', edgecolor='black', alpha=0.7)
    plt.xlabel("GC Content (%)")
    plt.ylabel("Number of Sequences")
    plt.title("HISTOGRAM \n GC Content Distribution of DNA Sequences")
    plt.grid(True)

    # Save plot
    plt.savefig(paths.GC_HISTOGRAM, dpi=300)
    print(f"Histogram plot saved to {paths.GC_HISTOGRAM}")

    plt.show()

def line(gc_contents):
    """
    Plot and save GC content as a line graph.

    :param gc_contents: List of GC content percentages.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(gc_contents, marker='o', linestyle='-', color='b', markersize=4)
    plt.xlabel("Sequence Index")
    plt.ylabel("GC Content (%)")
    plt.title("LINE PLOT \n GC Content of Each DNA Sequence")
    plt.grid(True)

    # Save plot
    plt.savefig(paths.GC_LINE_PLOT, dpi=300)
    print(f"Line plot saved to {paths.GC_LINE_PLOT}")

    plt.show()

def scatter(gc_contents):
    """
    Plot and save GC content as a scatter plot.

    :param gc_contents: List of GC content percentages.
    """
    plt.figure(figsize=(10, 5))
    plt.scatter(range(len(gc_contents)), gc_contents, color='r', alpha=0.6)
    plt.xlabel("Sequence Index")
    plt.ylabel("GC Content (%)")
    plt.title("SCATTER PLOT \n GC Content of Each DNA Sequence")
    plt.grid(True)

    # Save plot
    plt.savefig(paths.GC_SCATTER_PLOT, dpi=300)
    print(f"Scatter plot saved to {paths.GC_SCATTER_PLOT}")

    plt.show()
