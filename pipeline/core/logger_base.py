# import logging

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s %(levelname)s [%(name)s] [%(module)s] %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
# )

# logger = logging.getLogger("pipepile")

from prefect.logging import get_logger

logger = get_logger()
