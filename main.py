# -*- coding: utf-8 -*-
"""
DNA Sequence Analysis Pipeline

This script runs the full DNA sequence analysis pipeline, including:
- GC content analysis
- Dinucleotide frequency computation
- K-mer frequency detection (k=3,4,5)
- Palindrome sequence detection
- Unusual pattern analysis (repeats, AT/GC-rich, motifs)

Usage:
- Run `python main.py` to execute the full analysis.
- Outputs are stored in the `outputs/` directory.

@author: AnushKolakalur
"""

from pkg.utils import paths, read_json  
from pkg.gc_analysis import compute_gc, plot_gc
from pkg.dinucleotide_analysis import compute_dinucleotide
from pkg.kmer_analysis import compute_kmer
from pkg.pattern_analysis import detect_palindromes, detect_unusual_patterns

class DNAAnalyzer:
    """
    A class to run the complete DNA sequence analysis pipeline.
    """

    def __init__(self):
        """Initialize the DNAAnalyzer and load sequences."""
        self.sequences = read_json.load_sequences()

    def analyze_gc_content(self):
        """Compute GC content and generate plots."""
        gc_distribution = compute_gc.distribution(self.sequences)
        compute_gc.summary_statistics(gc_distribution)
        plot_gc.histogram(gc_distribution)
        plot_gc.line(gc_distribution)
        plot_gc.scatter(gc_distribution)

    def analyze_dinucleotides(self):
        """Compute and save dinucleotide frequencies."""
        dinucleotide_counts = compute_dinucleotide.compute_dinucleotide_frequencies(self.sequences)
        dinucleotide_counts.to_json(paths.DINUCLEOTIDE_JSON, orient="records", indent=4)

    def analyze_kmers(self):
        """Compute and save k-mer frequencies."""
        compute_kmer.save_kmer_results(self.sequences)

    def detect_palindromes(self):
        """Detect and save palindromic sequences."""
        detect_palindromes.save_palindrome_results(self.sequences)

    def detect_unusual_patterns(self):
        """Detect and save unusual DNA patterns."""
        detect_unusual_patterns.save_unusual_patterns(self.sequences)

    def run_pipeline(self):
        """Run the full DNA analysis pipeline."""
        print("\nStarting DNA Sequence Analysis...\n")
        self.analyze_gc_content()
        self.analyze_dinucleotides()
        self.analyze_kmers()
        self.detect_palindromes()
        self.detect_unusual_patterns()
        print("\nAnalysis Completed! Results saved in `outputs/`.")

if __name__ == "__main__":
    analyzer = DNAAnalyzer()
    analyzer.run_pipeline()
