# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 14:12:31 2025

@author: AnushKolakalur
"""
from data import read_json

file_path = "data/dna_sequences.json" 
sequences = read_json.load_sequences(file_path)

#test = sequences[1][:5]

from pkg.gc_analysis import compute_gc

# Compute GC content
gc_distribution = compute_gc.gc_distribution(sequences)

# Compute summary statistics
summary = compute_gc.gc_summary_statistics(gc_distribution)

# Print summary
print(f"GC Content Statistics:\nMean: {summary['mean_gc']:.2f}%\n"
      f"Min: {summary['min_gc']:.2f}%\nMax: {summary['max_gc']:.2f}%\n"
      f"Standard Deviation: {summary['std_gc']:.2f}")

# Plot GC content distribution
compute_gc.plot_histogram(gc_distribution)

compute_gc.plot_line(gc_distribution)

compute_gc.plot_scatter(gc_distribution)
