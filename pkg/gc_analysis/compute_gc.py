"""
compute_gc.py

This script computes the GC content for DNA sequences and provides summary statistics.

Functions:
- distribution(sequences): Calculates GC content for each sequence.
- summary_statistics(gc_contents): Computes mean, min, max, and std of GC content.
"""

import json
from pkg.utils import paths

def distribution(sequences):
    """
    Compute GC content percentage for each sequence.

    :param sequences: List of DNA sequences.
    :return: List of GC content percentages.
    """
    return [(seq.count("G") + seq.count("C")) / len(seq) * 100 for seq in sequences]

def summary_statistics(gc_contents):
    """
    Compute summary statistics for GC content across all sequences.

    :param gc_contents: List of GC content percentages.
    :return: Dictionary containing mean, min, max, and standard deviation.
    """
    import numpy as np
    summary = {
        "mean_gc": np.mean(gc_contents),
        "min_gc": np.min(gc_contents),
        "max_gc": np.max(gc_contents),
        "std_gc": np.std(gc_contents)
    }

    # Save GC summary statistics as JSON
    with open(paths.GC_SUMMARY_JSON, "w") as f:
        json.dump(summary, f, indent=4)

    print(f"\nGC Content Summary saved to {paths.GC_SUMMARY_JSON}")

    return summary
