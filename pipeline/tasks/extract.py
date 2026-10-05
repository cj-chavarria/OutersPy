from prefect import flow, task
from pydantic import BaseModel, ValidationError
from pydantic_core import PydanticSerializationError

from pipeline.clients.jpl_client import JPLService
from pipeline.core.logger_base import logger
from pipeline.utils.get_times import start_time, stop_time


class HorizonResponse(BaseModel):
    signature: dict
    result: str


SUN = "@sun"
PLANETS = {
    # {Name: (Close Approach Name, Horizon ID)}
    "Mercury": ("Merc", 199),
    "Venus": ("Venus", 299),
    "Earth": ("Earth", 399),
    "Mars": ("Mars", 499),
    "Jupiter": ("Juptr", 599),
    "Saturn": ("Satrn", 699),
    "Uranus": ("Urnus", 799),
    "Neptune": ("Neptn", 899),
}

jpl = JPLService(start_time=start_time, stop_time=stop_time)


@task(log_prints=True)
def extract_planet_orbit(planet: int | str) -> str:
    try:
        response = jpl.horizon(center=SUN, body=planet)
        horizon_respose = HorizonResponse.model_validate(response.json())

        data = horizon_respose.model_dump_json(warnings="error")
    except ValidationError, PydanticSerializationError:
        logger.warning(
            "A error ocurred during data validation from the Horizon response. "
        )

    return data


if __name__ == "__main__":
    pass
