"""
detect_unusual_patterns.py

This script detects unusual DNA patterns including:
- Repetitive sequences (microsatellites)
- AT- or GC-rich regions
- Low complexity sequences (single/double base dominance)
- Known biological motifs (TATA box, CpG islands)

Functions:
- find_repetitive_sequences(sequence): Detects short tandem repeats (STRs).
- find_at_gc_rich_regions(sequence, window_size=50, threshold=0.8): Identifies AT- or GC-rich regions.
- find_low_complexity_regions(sequence, threshold=0.8): Detects sequences dominated by 1-2 bases.
- find_known_motifs(sequence): Searches for biologically significant motifs.
- detect_unusual_patterns(sequences): Runs all detection methods per sequence.
- save_unusual_patterns(sequences): Saves results to JSON.
"""

import json
import re
from pkg.utils import paths

def find_repetitive_sequences(sequence):
    """
    Detects short tandem repeats (STRs) where a 2-6 base sequence is repeated ≥ 4 times.

    :param sequence: DNA sequence (string).
    :return: List of repetitive sequences found.
    """
    repeats = []
    for size in range(2, 7):  # Check repeat units of size 2 to 6
        pattern = re.compile(rf'([ACGT]{{{size}}})\1{{3,}}')  # Look for 4+ repeats
        matches = pattern.findall(sequence)
        repeats.extend(matches)
    return list(set(repeats))  # Remove duplicates

def find_at_gc_rich_regions(sequence, window_size=50, threshold=0.8):
    """
    Identifies regions that are AT-rich or GC-rich (≥ 80% A+T or G+C in a 50-base window).

    :param sequence: DNA sequence (string).
    :param window_size: Size of the sliding window.
    :param threshold: Minimum proportion of AT or GC to qualify as rich (default: 80%).
    :return: Dictionary of AT-rich and GC-rich regions.
    """
    at_rich = []
    gc_rich = []

    for i in range(len(sequence) - window_size + 1):
        window = sequence[i:i + window_size]
        at_count = window.count("A") + window.count("T")
        gc_count = window.count("G") + window.count("C")

        if at_count / window_size >= threshold:
            at_rich.append(window)
        if gc_count / window_size >= threshold:
            gc_rich.append(window)

    return {"AT_rich": at_rich, "GC_rich": gc_rich}

def find_low_complexity_regions(sequence, threshold=0.8):
    """
    Detects low complexity regions where 1 or 2 bases dominate ≥ 80% of the sequence.

    :param sequence: DNA sequence (string).
    :param threshold: Minimum proportion for dominance.
    :return: List of low complexity regions.
    """
    low_complexity = []
    window_size = 50  # Check in 50-base windows

    for i in range(len(sequence) - window_size + 1):
        window = sequence[i:i + window_size]
        base_counts = {base: window.count(base) for base in set(window)}

        if any(count / window_size >= threshold for count in base_counts.values()):
            low_complexity.append(window)

    return low_complexity

def find_known_motifs(sequence):
    """
    Detects biologically significant motifs in DNA.

    :param sequence: DNA sequence (string).
    :return: List of detected motifs.
    """
    motifs = []
    motif_patterns = {
        "TATA Box": r"TATA(?:AA)?",  # TATA or TATAAA
        "CpG Island": r"(CG){3,}",   # CpG repeats
    }

    for name, pattern in motif_patterns.items():
        if re.search(pattern, sequence):
            motifs.append(name)

    return motifs

def detect_unusual_patterns(sequences):
    """
    Detects unusual DNA patterns in each sequence.

    :param sequences: List of DNA sequences.
    :return: List of dictionaries containing unusual patterns per sequence.
    """
    all_patterns = []

    for seq in sequences:
        sequence_patterns = {
            "repetitive_sequences": find_repetitive_sequences(seq),
            "AT_GC_rich_regions": find_at_gc_rich_regions(seq),
            "low_complexity_regions": find_low_complexity_regions(seq),
            "known_motifs": find_known_motifs(seq),
        }
        all_patterns.append(sequence_patterns)

    return all_patterns

def save_unusual_patterns(sequences):
    """
    Detect unusual patterns in DNA sequences and save as JSON.

    :param sequences: List of DNA sequences.
    """
    pattern_results = detect_unusual_patterns(sequences)

    # Save results as JSON
    with open(paths.UNUSUAL_PATTERNS_JSON, "w") as f:
        json.dump(pattern_results, f, indent=4)

    print(f"\nUnusual patterns saved to {paths.UNUSUAL_PATTERNS_JSON}")
