import json

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, "r") as file:
        return json.load(file)

def save_json(file_path, data):
    """Save JSON data to a file."""
    with open(file_path, "w") as outfile:
        json.dump(data, outfile, indent=4)


def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading JSON from {file_path}: {e}")
        return None

def save_json(file_path, data):
    """Save JSON data to a file."""
    try:
        with open(file_path, "w") as outfile:
            json.dump(data, outfile, indent=4)
    except (PermissionError, OSError) as e:
        print(f"Error saving JSON to {file_path}: {e}")
