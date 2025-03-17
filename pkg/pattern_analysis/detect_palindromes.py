"""
detect_palindromes.py

Optimized script for detecting palindromic sequences in DNA that:
- Are at least 20 bases long.
- Contain at least 3 different nucleotide bases (A, C, T, G).
- Match their reverse complement.
- Cleans sequences by removing invalid bases instead of skipping them.

Functions:
- reverse_complement(sequence): Computes the reverse complement of a DNA sequence.
- clean_sequence(sequence): Removes invalid characters (keeps only A, T, C, G).
- find_palindromes(sequences, min_length=20): Detects palindromes efficiently.
- save_palindrome_results(sequences): Saves detected palindromes as JSON.
"""

import json
from pkg.utils import paths

def reverse_complement(sequence):
    """
    Compute the reverse complement of a DNA sequence.

    :param sequence: DNA sequence (string).
    :return: Reverse complement of the sequence (string).
    """
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement.get(base, "") for base in reversed(sequence) if base in complement)

def clean_sequence(sequence):
    """
    Remove invalid characters from a DNA sequence, keeping only A, T, C, and G.

    :param sequence: DNA sequence (string).
    :return: Cleaned sequence containing only valid bases.
    """
    valid_bases = {"A", "T", "C", "G"}
    cleaned_seq = "".join(base for base in sequence if base in valid_bases)

    if len(cleaned_seq) < 20:
        print(f"Warning: Sequence too short after cleaning. Skipping.")
        return None  # If the cleaned sequence is too short, return None
    
    return cleaned_seq

def find_palindromes(sequences, min_length=20):
    """
    Detect palindromic sequences efficiently using a sliding window approach.

    :param sequences: List of DNA sequences.
    :param min_length: Minimum palindrome length (default: 20).
    :return: List of dictionaries, each containing palindromes for a sequence.
    """
    all_palindromes = []

    for seq in sequences:
        seq = seq.upper()  # Ensure uppercase
        cleaned_seq = clean_sequence(seq)  # Remove invalid characters

        if not cleaned_seq:
            all_palindromes.append({"palindromes": [], "warning": "Sequence contained mostly invalid bases"})
            continue

        sequence_palindromes = []
        rev_complement_seq = reverse_complement(cleaned_seq)  # Compute reverse complement once

        for i in range(len(cleaned_seq) - min_length + 1):
            for j in range(min_length, len(cleaned_seq) - i + 1):
                candidate = cleaned_seq[i:i+j]

                # Skip if it doesn't have at least 3 different bases
                if len(set(candidate)) < 3:
                    continue

                # Compare with precomputed reverse complement instead of computing for each substring
                if candidate == rev_complement_seq[len(cleaned_seq)-i-j:len(cleaned_seq)-i]:
                    sequence_palindromes.append(candidate)

        all_palindromes.append({"palindromes": sequence_palindromes})

    return all_palindromes

def save_palindrome_results(sequences):
    """
    Detect palindromes in sequences and save results to JSON.

    :param sequences: List of DNA sequences.
    """
    palindrome_results = find_palindromes(sequences)

    # Save results as JSON
    with open(paths.PALINDROMES_JSON, "w") as f:
        json.dump(palindrome_results, f, indent=4)

    print(f"\nPalindrome sequences saved to {paths.PALINDROMES_JSON}")
