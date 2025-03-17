import os

# === BASE DIRECTORIES ===
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")) # Root project directory
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

# === DATA FILE PATHS ===
DNA_SEQUENCE_FILE = os.path.join(DATA_DIR, "dna_sequences.json")

# === GC CONTENT OUTPUT PATHS ===
GC_ANALYSIS_DIR = os.path.join(OUTPUT_DIR, "gc_analysis")
GC_HISTOGRAM = os.path.join(GC_ANALYSIS_DIR, "gc_histogram.png")
GC_LINE_PLOT = os.path.join(GC_ANALYSIS_DIR, "gc_line_plot.png")
GC_SCATTER_PLOT = os.path.join(GC_ANALYSIS_DIR, "gc_scatter_plot.png")
GC_SUMMARY_JSON = os.path.join(GC_ANALYSIS_DIR, "gc_summary.json")

# === DINUCLEOTIDE ANALYSIS OUTPUT PATHS ===
DINUCLEOTIDE_ANALYSIS_DIR = os.path.join(OUTPUT_DIR, "dinucleotide_analysis")
DINUCLEOTIDE_JSON = os.path.join(DINUCLEOTIDE_ANALYSIS_DIR, "dinucleotide_frequencies.json")

# Ensure directories exist
os.makedirs(GC_ANALYSIS_DIR, exist_ok=True)
os.makedirs(DINUCLEOTIDE_ANALYSIS_DIR, exist_ok=True)

# === K-MER ANALYSIS OUTPUT PATHS ===
KMER_ANALYSIS_DIR = os.path.join(OUTPUT_DIR, "kmer_analysis")
KMER_JSON = os.path.join(KMER_ANALYSIS_DIR, "kmer_frequencies.json")

# Ensure directories exist
os.makedirs(KMER_ANALYSIS_DIR, exist_ok=True)

# === PATTERN ANALYSIS OUTPUT PATHS ===
PATTERN_ANALYSIS_DIR = os.path.join(OUTPUT_DIR, "pattern_analysis")
PALINDROMES_JSON = os.path.join(PATTERN_ANALYSIS_DIR, "palindromes.json")

# Ensure directory exists
os.makedirs(PATTERN_ANALYSIS_DIR, exist_ok=True)
