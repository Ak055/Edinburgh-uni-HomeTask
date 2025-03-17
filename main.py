# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 14:12:31 2025

@author: AnushKolakalur
"""
import json
from pkg.utils import paths, read_json  
from pkg.gc_analysis import compute_gc, plot_gc
from pkg.dinucleotide_analysis import compute_dinucleotide

# === LOAD DATA ===
sequences = read_json.load_sequences()

# === COMPUTE GC CONTENT ===
gc_distribution = compute_gc.distribution(sequences)
summary = compute_gc.summary_statistics(gc_distribution)

# Save GC summary statistics as JSON
gc_summary_path = paths.GC_SUMMARY_JSON
with open(gc_summary_path, "w") as f:
    json.dump(summary, f, indent=4)

print(f"\nGC Content Summary saved to {gc_summary_path}")

# Generate and save GC content plots
plot_gc.histogram(gc_distribution)
plot_gc.line(gc_distribution)
plot_gc.scatter(gc_distribution)

# === COMPUTE DINUCLEOTIDE FREQUENCIES ===
dinucleotide_counts = compute_dinucleotide.compute_dinucleotide_frequencies(sequences)

# Print first 5 rows of the dinucleotide frequency DataFrame
print("\nDinucleotide Frequency DataFrame (First 5 Sequences):")
print(dinucleotide_counts.head())

# Save the dinucleotide frequency DataFrame as a JSON file
dinucleotide_counts.to_json(paths.DINUCLEOTIDE_JSON, orient="records", indent=4)

print(f"\nDinucleotide frequencies saved to {paths.DINUCLEOTIDE_JSON}")


