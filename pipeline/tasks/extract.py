from datetime import UTC, datetime, timedelta

from pipeline.clients.jpl_client import JPLService

now = datetime.now(tz=UTC)
week = now + timedelta(days=6)


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
    with JPLService(start_time=now, stop_time=week) as jpl:
        orbit = jpl.orbit_elements(center="@sun", body=PLANETS_ID["Earth"][1])

    print(orbit.get("result"))
