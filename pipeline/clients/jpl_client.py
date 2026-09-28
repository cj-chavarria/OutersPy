from datetime import date

import httpx


class JPLService:
    def __init__(self, start_time: date, stop_time: date):
        self.client = httpx.Client()
        self.start_time = start_time.strftime("%Y-%m-%d")
        self.stop_time = stop_time.strftime("%Y-%m-%d")

    def orbit_elements(self, center: str, body: str):
        response = self.client.get(
            url="https://ssd.jpl.nasa.gov/api/horizons.api",
            params={
                "format": "json",
                "COMMAND": body,
                "EPHEM_TYPE": "ELEMENTS",
                "CENTER": center,
                "START_TIME": self.start_time,
                "STOP_TIME": self.stop_time,
                "STEP_SIZE": "1d",
                "CSV_FORMAT": "YES",
                "OUT_UNITS": "AU-D",
            },
        )
        response.raise_for_status()
        return response.json()

    def close_approaches(self, body: str, dist_max: float = 0.05):
        response = self.client.get(
            url="https://ssd-api.jpl.nasa.gov/cad.api",
            params={
                "body": body,
                "date-min": self.start_time,
                "date-max": self.stop_time,
                "sort": "dist-min",
                "diameter": True,
                "dist-max": dist_max,
            },
        )
        response.raise_for_status()
        return response.json()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
