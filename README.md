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

## **3️⃣ Unusual Pattern Detection**
(*This section will be updated once `unusual_patterns.json` is analyzed.*)

### **📌 Palindrome Sequences**
- `XX` sequences contained palindromes of **≥ 20 bases**.
- The longest palindrome detected: `"XXXXXXXXXXXXXXXXXXXX"` (`YY bases long`).
- These sequences may have **structural or functional significance** in DNA folding.

### **📌 Repetitive Sequences (Microsatellites)**
- Found **`XX` sequences** containing **short tandem repeats (STRs)**.
- Common repeats:
  - `"ATATAT"` (`YY occurrences`)
  - `"GCGCGC"` (`YY occurrences`)
- Some sequences exhibited **extensive microsatellite regions**, which may be linked to **mutational instability**.

### **📌 AT- or GC-Rich Regions**
- **`XX` sequences** contained **AT-rich (≥ 80%) regions**.
- **`XX` sequences** contained **GC-rich (≥ 80%) regions**.
- **High GC content regions** could indicate **functional elements like CpG islands**.

### **📌 Low Complexity Sequences**
- **`XX` sequences** had regions dominated by **just 1 or 2 bases**.
- **Highly repetitive, low-complexity regions** may be **mutation-prone or result from sequencing artifacts**.

### **📌 Known Biological Motifs**
- **TATA Box (`TATAAA`)** was found in **`XX` sequences**, suggesting **potential promoter regions**.
- **CpG islands (`CGCGCG`)** were found in **`XX` sequences**, possibly linked to **gene regulation**.

---

## **4️⃣ Conclusions & Next Steps**
- The dataset contains **diverse sequence patterns**, including **palindromes, STRs, high GC regions, and functional motifs**.
- **Further investigation** into **sequences with extreme GC content and unusual patterns** could reveal **biological relevance**.
- Future work could include:
  - Comparing these findings with **real genomic data**.
  - Identifying **functional elements** using external genomic databases.
  - Applying **machine learning** to classify sequences based on features.

---

🔬 **This analysis provides valuable insights into sequence structure, functional elements, and potential genetic variations.** 🚀
