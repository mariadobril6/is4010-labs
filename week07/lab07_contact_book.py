
import json
import os


def save_contacts_to_json(contacts, filename):
    """Write the contacts list to filename as indented JSON."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)


def load_contacts_from_json(filename):
    """Return contacts from filename, or an empty list if it does not exist."""
    if not os.path.exists(filename):
        return []

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
