import numpy as np
import matplotlib.pyplot as plt

def gc_content(sequence):
    """
    Calculate GC content percentage in a DNA sequence.

    :param sequence: DNA sequence (string).
    :return: GC content percentage.
    """
    gc_count = sum(1 for base in sequence if base in 'GC')
    return (gc_count / len(sequence)) * 100

def gc_distribution(sequences):
    """
    Compute the GC content percentage for all sequences.

    :param sequences: List of DNA sequences.
    :return: List of GC content percentages.
    """
    return [gc_content(seq) for seq in sequences]

def gc_summary_statistics(gc_contents):
    """
    Compute summary statistics for GC content.

    :param gc_contents: List of GC content percentages.
    :return: Dictionary with mean, min, max, std.
    """
    return {
        "mean_gc": np.mean(gc_contents),
        "min_gc": np.min(gc_contents),
        "max_gc": np.max(gc_contents),
        "std_gc": np.std(gc_contents)
    }

def plot_histogram(gc_contents):
    """
    Plot a histogram of GC content distribution.

    :param gc_contents: List of GC content percentages.
    """
    plt.figure(figsize=(8, 5))
    plt.hist(gc_contents, bins='auto', edgecolor='black', alpha=0.7)
    plt.xlabel("GC Content (%)")
    plt.ylabel("Number of Sequences")
    plt.title("GC Content Distribution of DNA Sequences")
    plt.grid(True)
    plt.show()
    
def plot_line(gc_contents):
    """
    Plot GC content for all sequences as a line graph.

    :param gc_contents: List of GC content percentages.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(gc_contents, marker='o', linestyle='-', color='b', markersize=4)  # Line with dots
    plt.xlabel("Sequence Index")
    plt.ylabel("GC Content (%)")
    plt.title("GC Content of Each DNA Sequence")
    plt.grid(True)
    plt.show()
    
def plot_scatter(gc_contents):
    """
    Plot GC content for all sequences as a scatter plot.

    :param gc_contents: List of GC content percentages.
    """
    plt.figure(figsize=(10, 5))
    plt.scatter(range(len(gc_contents)), gc_contents, color='r', alpha=0.6)  # Red dots
    plt.xlabel("Sequence Index")
    plt.ylabel("GC Content (%)")
    plt.title("GC Content of Each DNA Sequence")
    plt.grid(True)
    plt.show()



