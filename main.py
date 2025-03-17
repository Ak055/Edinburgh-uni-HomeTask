# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 14:12:31 2025

@author: AnushKolakalur
"""
from pkg.utils import paths, read_json  
from pkg.gc_analysis import compute_gc, plot_gc
from pkg.dinucleotide_analysis import compute_dinucleotide
from pkg.kmer_analysis import compute_kmer
from pkg.pattern_analysis import detect_palindromes
from pkg.pattern_analysis import detect_unusual_patterns

# === LOAD DATA ===
sequences = read_json.load_sequences()
#sequences = [seq[:50] for seq in sequences[:10]]

# === COMPUTE GC CONTENT ===
gc_distribution = compute_gc.distribution(sequences)
summary = compute_gc.summary_statistics(gc_distribution)

# Generate and save GC content plots
plot_gc.histogram(gc_distribution)
plot_gc.line(gc_distribution)
plot_gc.scatter(gc_distribution)

# === COMPUTE DINUCLEOTIDE FREQUENCIES ===
dinucleotide_counts = compute_dinucleotide.compute_dinucleotide_frequencies(sequences)

# Save the dinucleotide frequency DataFrame as a JSON file
dinucleotide_counts.to_json(paths.DINUCLEOTIDE_JSON, orient="records", indent=4)

# === COMPUTE K-MER FREQUENCIES ===
compute_kmer.save_kmer_results(sequences)

# === DETECT PALINDROMIC SEQUENCES ===
#detect_palindromes.save_palindrome_results(sequences)

# === DETECT UNUSUAL PATTERNS ===
detect_unusual_patterns.save_unusual_patterns(sequences)
