
import json


class FavoritesManager:
    """Manage saved favorite locations in a JSON file."""

    def __init__(self, filename):
        self.filename = filename
        self.favorites = {}

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, dict):
                    self.favorites = data
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            self.favorites = {}

    def _save(self):
        """Save favorites to the JSON file."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.favorites, file, indent=4)

    def add(self, name, location):
        """Add a favorite unless its name already exists."""
        key = name.casefold()
        if key in self.favorites:
            return False

        self.favorites[key] = location
        self._save()
        return True

    def remove(self, name):
        """Remove a favorite by name, ignoring capitalization."""
        key = name.casefold()
        if key not in self.favorites:
            return False

        del self.favorites[key]
        self._save()
        return True

    def list_all(self):
        """Return the saved favorites and their locations."""
        return self.favorites.copy()

    def get_location(self, name):
        """Return a favorite's location, ignoring capitalization."""
        return self.favorites.get(name.casefold())

