# 🧬 DNA Sequence Analysis Pipeline

## **📌 Overview**
This project performs **comprehensive DNA sequence analysis**, including:
- **GC Content Analysis** (Distribution & Visualization)
- **Dinucleotide Frequency Computation**
- **K-mer Analysis (Top 5 for k=3, 4, 5)**
- **Palindrome Sequence Detection**
- **Unusual Pattern Analysis** (Microsatellites, AT/GC-Rich Regions, Low Complexity Sequences, and Known Motifs)

The entire pipeline is implemented in Python and saves outputs in **structured JSON files and visualized plots**.

---

## **📌 Installation**
### **🔹 Prerequisites**
Ensure you have **Python 3.x** installed. You can check by running:
```bash
python --version
```

### **🔹 Clone the Repository**
```bash
git clone https://github.com/Ak055/Edinburgh-uni-HomeTask.git
cd Edinburgh-uni-HomeTask
```

### **🔹 Install Dependencies**
Run the following command to install required packages:
```bash
pip install -r requirements.txt
```
---

## **📌 Usage**
### **Run the Full Analysis**
To execute the entire analysis pipeline, run:
```bash
python main.py
```
This will:
- Compute GC content and generate histograms.
- Analyze dinucleotide and k-mer frequencies.
- Detect palindromic sequences.
- Identify unusual patterns in sequences.
- Save results in the `outputs/` directory.

### **Expected Output Files**
| **File Name** | **Description** | **Location** |
|--------------|---------------|-------------|
| `gc_summary.json` | GC content summary (Mean, Min, Max, Std) | `outputs/gc_analysis/` |
| `dinucleotide_frequencies.json` | Per-sequence dinucleotide counts | `outputs/dinucleotide_analysis/` |
| `kmer_frequencies.json` | Top 5 k-mers for k=3,4,5 | `outputs/kmer_analysis/` |
| `palindromes.json` | List of detected palindromes per sequence | `outputs/pattern_analysis/` |
| `unusual_patterns.json` | List of microsatellites, low complexity regions, and motifs | `outputs/pattern_analysis/` |

---

## **📌 Key Findings**
This analysis produced **valuable insights into DNA sequence composition**:

### **🔬 GC Content**
- **Average GC Content**: `59.14%`
- **Lowest GC Content**: `35.70%`
- **Highest GC Content**: `83.30%`
- **Standard Deviation**: `6.99`
- The histogram suggests a **bimodal distribution**, indicating two distinct GC content groups.

### **🔬 K-mer Analysis (Most Frequent Substrings)**
| K-mer Length | Most Frequent K-mers |
|--------------|----------------------|
| **k=3** | `"CCC"`, `"GCC"`, `"CGC"` |
| **k=4** | `"CCCC"`, `"CGCC"`, `"GCCG"` |
| **k=5** | `"CCCCC"`, `"CCGCC"`, `"CGCCC"` |

### **🔬 Palindrome Detection**
- **5 sequences contained palindromes**.
- **Longest palindrome found**:  
  `"TAAACGGGCCTTAATATATATTAAGGCCCGTTTA"` (**34 bases long**).

### **🔬 Unusual Pattern Detection**
- **76 sequences had repetitive regions** (e.g., `"GGGGA"`, `"CGC"`).
- **AT-Rich regions found in 18,734 sequences**.
- **GC-Rich regions found in 32,669 sequences**.
- **Known motifs detected**:
  - `"TATA Box"` (Transcription start site).
  - `"CpG Island"` (Gene regulation).

---

## **📌 Project Structure**
```
Edinburgh-uni-HomeTask/
├── data/                      # Input sequences
│   ├── dna_sequences.json
├── outputs/                   # Results stored here
│   ├── gc_analysis/
│   ├── dinucleotide_analysis/
│   ├── kmer_analysis/
│   ├── pattern_analysis/
├── pkg/                        # Core analysis modules
│   ├── utils/
│   ├── gc_analysis/
│   ├── dinucleotide_analysis/
│   ├── kmer_analysis/
│   ├── pattern_analysis/
│   │   ├── detect_palindromes.py
│   │   ├── detect_unusual_patterns.py
│   │   ├── find_known_motifs.py
├── main.py                     # Runs the full analysis
├── README.md                    # Documentation
```

---

## **📌 Future Improvements**
- **Optimize performance** → Implement **parallel processing** to speed up computations.
- **Support for larger datasets** → Process **millions of sequences efficiently**.
- **Machine Learning Integration** → Classify DNA sequences based on detected patterns.

---

## **📌 License**
This project is open-source and available under the **MIT License**.

🚀 **Developed by [Anush Kolakalur]** 🔥
