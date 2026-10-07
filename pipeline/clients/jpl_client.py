import httpx2

from pipeline.core.logger_base import logger


class JPLService:
    def __init__(self, start_time: str, stop_time: str):
        self.client = httpx2.Client()
        self.start_time = start_time
        self.stop_time = stop_time

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def horizon(self, center: str, body: str | int) -> httpx2.Response:
        try:
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
        except httpx2.HTTPError as e:
            logger.error(e)
            raise

        return response

    def close_approaches(self, body: str, dist_max: float = 0.05) -> httpx2.Response:
        try:
            response = self.client.get(
                url="https://ssd-api.jpl.nasa.gov/cad.api",
                params={
                    "body": body,
                    "date-min": self.start_time,
                    "date-max": self.stop_time,
                    "sort": "dist-min",
                    "diameter": True,
                    "dist-max": dist_max,
                    "limit": 1,
                },
            )
            response.raise_for_status()
        except httpx2.HTTPError as e:
            logger.error(e)
            raise

        return response
