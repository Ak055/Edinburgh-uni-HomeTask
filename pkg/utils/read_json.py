import json
from pkg.utils import paths

def load_sequences():
    """
    Load DNA sequences from a JSON file.

    :return: List of DNA sequences.
    """
    with open(paths.DNA_SEQUENCE_FILE, 'r') as f:
        data = json.load(f)
    return data['sequences']
