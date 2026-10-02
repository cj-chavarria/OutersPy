from collections.abc import Generator

from pipeline.utils.get_dates import start_time, stop_time

PLANETS = {
    # {Horizon Name: (Close Approach Name, Horizon ID)}
    "Mercury": ("Merc", 199),
    "Venus": ("Venus", 299),
    "Earth": ("Earth", 399),
    "Mars": ("Mars", 499),
    "Jupiter": ("Juptr", 599),
    "Saturn": ("Satrn", 699),
    "Uranus": ("Urnus", 799),
    "Neptune": ("Neptn", 899),
}


def planets_orbits() -> Generator[str]:
    yield from PLANETS


if __name__ == "__main__":
    print(type(planets_orbits()))
