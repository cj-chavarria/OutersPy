from datetime import UTC, datetime, timedelta
from pprint import pprint

from pydantic import BaseModel

from pipeline.clients.jpl_client import JPLService

now = datetime.now(tz=UTC)
week = now + timedelta(days=6)


class HorizonResponse(BaseModel):
    signature: dict
    result: str


PLANETS_ID = {
    # {Horizon Name: (Close Approach Name, Horizon ID)}
    "Mercury": ("Merc", "199"),
    "Venus": ("Venus", "299"),
    "Earth": ("Earth", "399"),
    "Mars": ("Mars", "499"),
    "Jupiter": ("Juptr", "599"),
    "Saturn": ("Satrn", "699"),
    "Uranus": ("Urnus", "799"),
    "Neptune": ("Neptn", "899"),
}

if __name__ == "__main__":
    with JPLService(now, week) as jpl:
        response = jpl.orbit_elements(center="@sun", body=PLANETS_ID["Earth"][1])

    # pprint(response, sort_dicts=False)

    print(HorizonResponse.model_validate(response))
