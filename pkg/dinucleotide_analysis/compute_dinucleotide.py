"""
compute_dinucleotide.py

This script computes dinucleotide (2-mer) frequencies for each DNA sequence.

Functions:
- compute_dinucleotide_frequencies(sequences): Returns a DataFrame of dinucleotide counts.
"""

import json
import pandas as pd
from collections import Counter
from pkg.utils import paths

def compute_dinucleotide_frequencies(sequences):
    """
    Compute dinucleotide frequencies per sequence.

    :param sequences: List of DNA sequences.
    :return: Pandas DataFrame with dinucleotide counts for each sequence.
    """
    all_frequencies = []

    for seq in sequences:
        dinucleotide_counts = Counter()

        # Iterate through the sequence to extract dinucleotides
        for i in range(len(seq) - 1):
            dinucleotide = seq[i:i+2]  # Extract two-letter combination
            dinucleotide_counts[dinucleotide] += 1

        all_frequencies.append(dinucleotide_counts)

    df = pd.DataFrame(all_frequencies).fillna(0)  # Convert to DataFrame and replace NaNs with 0

    # Save the dinucleotide frequency DataFrame as a JSON file
    df.to_json(paths.DINUCLEOTIDE_JSON, orient="records", indent=4)

    print(f"\nDinucleotide frequencies saved to {paths.DINUCLEOTIDE_JSON}")

    return df
