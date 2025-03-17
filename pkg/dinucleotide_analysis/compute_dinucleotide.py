import pandas as pd
from collections import Counter
from pkg.utils import paths


VALID_BASES = {'A', 'T', 'G', 'C'}

def compute_dinucleotide_frequencies(sequences, normalize=False):
    """
    Compute the frequency of valid dinucleotides (AA, AT, AG, ...) for each sequence.

    :param sequences: List of DNA sequences.
    :param normalize: If True, returns relative frequency instead of raw counts.
    :return: Pandas DataFrame with valid dinucleotide frequencies per sequence.
    """
    all_frequencies = []
    expected_dinucleotides = {a + b for a in VALID_BASES for b in VALID_BASES}  # 16 valid dinucleotides

    for seq in sequences:
        dinucleotide_counts = Counter()
        total_dinucleotides = len(seq) - 1  # 999 for 1000-base sequence

        for i in range(total_dinucleotides):
            dinucleotide = seq[i:i+2]  # Extract two-letter combination

            if dinucleotide in expected_dinucleotides:  # Only count valid ones
                dinucleotide_counts[dinucleotide] += 1

        all_frequencies.append(dinucleotide_counts)
        
    df = pd.DataFrame(all_frequencies).fillna(0)  # Convert to DataFrame and replace NaNs with 0

    # Save the dinucleotide frequency DataFrame as a JSON file
    df.to_json(paths.DINUCLEOTIDE_JSON, orient="records", indent=4)

    print(f"\nDinucleotide frequencies saved to {paths.DINUCLEOTIDE_JSON}")

    return df







