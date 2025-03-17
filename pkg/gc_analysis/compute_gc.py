import json
import numpy as np
from pkg.utils import paths

def gc_content(sequence):
    """
    Calculate GC content percentage in a DNA sequence.

    :param sequence: DNA sequence (string).
    :return: GC content percentage.
    """
    gc_count = sum(1 for base in sequence if base in 'GC')
    return (gc_count / len(sequence)) * 100

def distribution(sequences):
    """
    Compute the GC content percentage for all sequences.

    :param sequences: List of DNA sequences.
    :return: List of GC content percentages.
    """
    return [gc_content(seq) for seq in sequences]

def summary_statistics(gc_contents):
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

    # Save GC summary as JSON
    with open(paths.GC_SUMMARY_JSON, "w") as f:
        json.dump(summary, f, indent=4)

    print(f"\nGC Content Summary saved to {paths.GC_SUMMARY_JSON}")
    
    return summary
    




