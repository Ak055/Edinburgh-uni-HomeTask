"""
compute_kmer.py

This script computes the most common k-mers (substrings of length k) per sequence.
It extracts k-mers of lengths k=3, k=4, and k=5 and identifies the top 5 most frequent.

Functions:
- extract_kmers(sequence, k): Extracts k-mers from a sequence.
- compute_kmer_frequencies(sequences): Finds the top 5 k-mers for each sequence.
- save_kmer_results(sequences): Saves the results as JSON.
"""

import json
from collections import Counter
from pkg.utils import paths

def extract_kmers(sequence, k):
    """
    Extract all k-mers of length k from a given DNA sequence.

    :param sequence: DNA sequence (string).
    :param k: Length of k-mer.
    :return: List of k-mers in the sequence.
    """
    return [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

def compute_kmer_frequencies(sequences, k_values=(3, 4, 5)):
    """
    Compute the top 5 most common k-mers for each sequence separately.

    :param sequences: List of DNA sequences.
    :param k_values: Tuple of k values to analyze.
    :return: List of dictionaries, each containing top 5 k-mers for k=3, 4, 5 in a sequence.
    """
    all_results = []

    for seq in sequences:
        sequence_kmer_results = {}

        for k in k_values:
            kmer_counts = Counter(extract_kmers(seq, k))  # Count k-mers in this sequence
            top_kmers = dict(kmer_counts.most_common(5))  # Get top 5 most common k-mers
            sequence_kmer_results[f"k={k}"] = top_kmers

        all_results.append(sequence_kmer_results)  # Add results for this sequence

    return all_results

def save_kmer_results(sequences):
    """
    Compute k-mer frequencies for each sequence and save as a JSON file.

    :param sequences: List of DNA sequences.
    """
    kmer_results = compute_kmer_frequencies(sequences)

    # Save results as JSON
    with open(paths.KMER_JSON, "w") as f:
        json.dump(kmer_results, f, indent=4)

    print(f"\nK-mer frequencies saved to {paths.KMER_JSON}")
