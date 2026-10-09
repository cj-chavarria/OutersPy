from prefect import task
from pydantic import BaseModel, ValidationError
from pydantic_core import PydanticSerializationError

from pipeline.clients.jpl_client import JPLService
from pipeline.core.logger_base import logger
from pipeline.utils.get_times import start_time, stop_time


class HorizonResponse(BaseModel):
    signature: dict[str, str]
    result: str


class CloseApproachesResponse(BaseModel):
    signature: dict[str, str]
    count: int
    fields: list[str] | None = None
    data: list[list[str | None]] | None = None


SOLAR_SYS_BARYCENTER = "@0"
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


@task
def extract_object_orbit(
    jpl: JPLService, object: int | str, center: str = SOLAR_SYS_BARYCENTER
) -> str | None:
    try:
        response = jpl.horizon(center=center, command=object)
        horizon_response = HorizonResponse.model_validate(response.json())

        data = horizon_response.model_dump_json(warnings="error")

    except (ValidationError, PydanticSerializationError) as e:
        logger.error(e)
        return None

    return data


@task
def extract_planet_ca(jpl: JPLService, planet: str) -> str | None:
    try:
        response = jpl.close_approaches(body=planet)
        ca_response = CloseApproachesResponse.model_validate(response.json())

        data = ca_response.model_dump_json(warnings="error")

    except (ValidationError, PydanticSerializationError) as e:
        logger.error(e)
        return None

    return data
