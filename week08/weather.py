import argparse
import os
import sys
from pathlib import Path

try:
    from .favorites import FavoritesManager
    from .weather_api import WeatherAPI, format_current_weather, format_forecast
except ImportError:
    from favorites import FavoritesManager
    from weather_api import WeatherAPI, format_current_weather, format_forecast


WEEK08_DIR = Path(__file__).resolve().parent
FAVORITES_FILE = WEEK08_DIR / "favorites.json"


def load_api_key():
    """Load the API key from the environment or local config.py."""
    key = os.environ.get("WEATHER_API_KEY")
    if key:
        return key

    try:
        import importlib.util

        config_path = WEEK08_DIR / "config.py"
        spec = importlib.util.spec_from_file_location("weather_config", config_path)

        if spec is None or spec.loader is None:
            return None

        config = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config)

        return (
            getattr(config, "WEATHER_API_KEY", None)
            or getattr(config, "API_KEY", None)
        )
    except (ImportError, OSError, AttributeError, SyntaxError):
        return None


def build_parser():
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(description="Command-line weather application")
    subparsers = parser.add_subparsers(dest="command", required=True)

    current_parser = subparsers.add_parser("current", help="Show current weather")
    current_parser.add_argument("location")

    forecast_parser = subparsers.add_parser("forecast", help="Show weather forecast")
    forecast_parser.add_argument("location")
    forecast_parser.add_argument("--days", type=int, default=3)

    favorites_parser = subparsers.add_parser("favorites", help="Manage favorites")
    favorites_subparsers = favorites_parser.add_subparsers(
        dest="favorites_command", required=True
    )

    add_parser = favorites_subparsers.add_parser("add")
    add_parser.add_argument("name")
    add_parser.add_argument("location")

    favorites_subparsers.add_parser("list")

    remove_parser = favorites_subparsers.add_parser("remove")
    remove_parser.add_argument("name")

    return parser


def main(argv=None) -> int:
    """Run the CLI and return 0 on success or 1 on operational failure."""
    parser = build_parser()
    args = parser.parse_args(argv)

    favorites = FavoritesManager(FAVORITES_FILE)

    if args.command == "favorites":
        if args.favorites_command == "add":
            if not favorites.add(args.name, args.location):
                print("Error: favorite already exists.", file=sys.stderr)
                return 1

            print(f"Added favorite: {args.name}")
            return 0

        if args.favorites_command == "list":
            for name, location in favorites.list_all().items():
                print(f"{name}: {location}")
            return 0

        if args.favorites_command == "remove":
            if not favorites.remove(args.name):
                print("Error: favorite not found.", file=sys.stderr)
                return 1

            print(f"Removed favorite: {args.name}")
            return 0

    api_key = load_api_key()
    if not api_key:
        print("Error: missing API key.", file=sys.stderr)
        return 1

    location = args.location
    favorite_location = favorites.get_location(location)
    if favorite_location is not None:
        location = favorite_location

    api = WeatherAPI(api_key)

    if args.command == "current":
        data = api.get_current_weather(location)
        if data is None:
            print("Error: weather request failed.", file=sys.stderr)
            return 1

        print(format_current_weather(data))
        return 0

    if args.command == "forecast":
        if not 1 <= args.days <= 3:
            print("Error: forecast days must be between 1 and 3.", file=sys.stderr)
            return 1

        data = api.get_forecast(location, args.days)
        if data is None:
            print("Error: forecast request failed.", file=sys.stderr)
            return 1

        print(format_forecast(data))
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
