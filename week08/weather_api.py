
import requests


class WeatherAPI:
    """Retrieve current weather and forecasts from WeatherAPI."""

    def __init__(self, api_key, base_url="https://api.weatherapi.com/v1"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def get_current_weather(self, location):
        """Return current weather data, or None if the request fails."""
        try:
            response = requests.get(
                f"{self.base_url}/current.json",
                params={"key": self.api_key, "q": location},
                timeout=10,
            )
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError):
            return None

    def get_forecast(self, location, days=3):
        """Return forecast data, or None if the request fails."""
        if not 1 <= days <= 3:
            raise ValueError("Forecast days must be between 1 and 3.")

        try:
            response = requests.get(
                f"{self.base_url}/forecast.json",
                params={"key": self.api_key, "q": location, "days": days},
                timeout=10,
            )
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError):
            return None


def format_current_weather(data):
    """Format current weather as city, country, temperature, and condition."""
    location = data["location"]
    current = data["current"]

    return (
        f"{location['name']}, {location['country']}: "
        f"{current['temp_f']}°F, {current['condition']['text']}"
    )


def format_forecast(data):
    """Format each forecast day with its high, low, and condition."""
    days = data["forecast"]["forecastday"]
    lines = []

    for day in days:
        date = day["date"]
        details = day["day"]
        high = details["maxtemp_f"]
        low = details["mintemp_f"]
        condition = details["condition"]["text"]

        lines.append(
            f"{date}: high {high}°F, low {low}°F, {condition}"
        )

    return "\n".join(lines)
