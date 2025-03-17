import json
from collections import Counter
from pkg.utils import paths

def extract_kmers(sequence, k):
    """
    Extract all k-mers of length k from a given DNA sequence.

    :param sequence: DNA sequence (string).
    :param k: Length of k-mer.
    :return: List of k-mers.
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
        sequence_kmer_results = {}  # Store results for this sequence

        for k in k_values:
            kmer_counts = Counter(extract_kmers(seq, k))  # Count k-mers in this sequence
            top_kmers = dict(kmer_counts.most_common(5))  # Get top 5 most common k-mers
            sequence_kmer_results[f"k={k}"] = top_kmers  # Store results

        all_results.append(sequence_kmer_results)  # Add to final results

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


