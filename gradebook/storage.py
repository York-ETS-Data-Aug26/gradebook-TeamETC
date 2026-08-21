"""Loading and saving roster data. Owner: B."""
import json
from json import JSONDecodeError

from gradebook.errors import StorageError


def load(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        #will return empty dictionary if no file exist
        return {}
    except JSONDecodeError:
        #text is broken and cannot be parse in file will output error
        raise StorageError


def save(path, roster):
    with open(path, 'w') as f:
        json.dump(roster, f, indent=4)