# HomeTask

# Summary of Findings

## **1️⃣ Overview**
This report summarizes key findings from the analysis of **200 DNA sequences**, each **1000 bases long**. The analysis included:
- **GC Content Distribution**
- **Dinucleotide Frequencies**
- **K-mer Analysis (Top 5 for k=3,4,5)**
- **Palindrome Detection**
- **Unusual Pattern Detection** (Repeats, AT/GC-Rich regions, Low Complexity, Biological Motifs)

---

## **2️⃣ Key Findings**

### **📌 GC Content Distribution**
- **Average GC Content**: 59.14%
- **Lowest GC Content**: 35.70%
- **Highest GC Content**: 83.30%
- **Standard Deviation**: 6.99
- The histogram indicates a **bimodal distribution**, suggesting the presence of sequences with distinct GC content groups.
- The **line and scatter plots show variability in GC content** across sequences.

### **📌 Dinucleotide Frequency Analysis**
- The **most frequent dinucleotide pairs** were:
  - `"GG"` (`112 occurrences`)
  - `"GC"` (`112 occurrences`)
  - `"CC"` (`151 occurrences`)
- The **least frequent dinucleotide pairs** included:
  - `"TA"` (`13 occurrences`)
  - `"AA"` (`21 occurrences`)
  - `"AT"` (`24 occurrences`)
- Some **unexpected characters (`EC`, `NG`, `OG`) appeared**, suggesting that **some sequences contain invalid bases**.

### **📌 K-mer Analysis (k=3,4,5)**
- The most frequent **3-mers (k=3)**:
  - `"CCC"` (`64 occurrences`)
  - `"GCC"` (`49 occurrences`)
  - `"CGC"` (`38 occurrences`)
- The most frequent **4-mers (k=4)**:
  - `"CCCC"` (`28 occurrences`)
  - `"CGCC"` (`23 occurrences`)
  - `"GCCG"` (`20 occurrences`)
- The most frequent **5-mers (k=5)**:
  - `"CCCCC"` (`13 occurrences`)
  - `"CCGCC"` (`11 occurrences`)
  - `"CGCCC"` (`10 occurrences`)
- The **dominance of C and G** in k-mers suggests the presence of **high GC-content regions**.

---

## **📌 Unusual Pattern Detection**
This section highlights unusual sequence patterns, including repetitive sequences, AT/GC-rich regions, low complexity regions, and known biological motifs.

### **🔍 Palindrome Sequences**
- **Total sequences with palindromes**: **5** sequences contained at least one palindrome.
- **Longest palindrome detected**:  
  `"TAAACGGGCCTTAATATATATTAAGGCCCGTTTA"` (**34 bases long**).
- **Palindromes were relatively rare**, suggesting they may be associated with **specific structural or functional elements**.

### **🔍 Repetitive Sequences (Microsatellites)**
- **76 unique repetitive sequences** detected.
- Common repeats included:
  - `"GGGGA"`
  - `"CGC"`
  - `"GAGA"`
  - `"TTTT"`
  - `"AATAAT"`
  - `"GCCG"`
- **Repeats may indicate mutational hotspots** or structural stability in DNA.

### **🔍 AT- or GC-Rich Regions**
- **AT-rich sequences** (≥ 80% A/T content): **18,734 sequences**.
- **GC-rich sequences** (≥ 80% G/C content): **32,669 sequences**.
- **GC-rich regions may indicate functional elements like CpG islands**, known to affect gene expression.

### **🔍 Low Complexity Sequences**
- **16 sequences** contained **low-complexity regions**.
- These were dominated by **just 1 or 2 bases**, including:
  - `"AAAAAA"`
  - `"GTGTGT"`
- **Such regions may be prone to mutations** or sequencing artifacts.

### **🔍 Known Biological Motifs**
- **Motifs detected in sequences**:
  - **TATA Box** (suggests potential promoter regions).
  - **CpG Islands** (associated with gene regulation and methylation).

---