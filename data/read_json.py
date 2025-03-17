import json

def load_sequences(file_path):
    """
    Load DNA sequences from a JSON file.

    :param file_path: Path to the JSON file.
    :return: List of DNA sequences.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data['sequences']