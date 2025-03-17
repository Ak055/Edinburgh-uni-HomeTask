import matplotlib.pyplot as plt

def histogram(gc_contents):
    """
    Plot a histogram of GC content distribution.

    :param gc_contents: List of GC content percentages.
    """
    plt.figure(figsize=(8, 5))
    plt.hist(gc_contents, bins='auto', edgecolor='black', alpha=0.7)
    plt.xlabel("GC Content (%)")
    plt.ylabel("Number of Sequences")
    plt.title("HISTOGRAM \n GC Content Distribution of DNA Sequences")
    plt.grid(True)
    plt.show()
    
def line(gc_contents):
    """
    Plot GC content for all sequences as a line graph.

    :param gc_contents: List of GC content percentages.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(gc_contents, marker='o', linestyle='-', color='b', markersize=4)  # Line with dots
    plt.xlabel("Sequence Index")
    plt.ylabel("GC Content (%)")
    plt.title("LINE PLOT \n GC Content of Each DNA Sequence")
    plt.grid(True)
    plt.show()
    
def scatter(gc_contents):
    """
    Plot GC content for all sequences as a scatter plot.

    :param gc_contents: List of GC content percentages.
    """
    plt.figure(figsize=(10, 5))
    plt.scatter(range(len(gc_contents)), gc_contents, color='r', alpha=0.6)  # Red dots
    plt.xlabel("Sequence Index")
    plt.ylabel("GC Content (%)")
    plt.title("SCATTER PLOT \n GC Content of Each DNA Sequence")
    plt.grid(True)
    plt.show()