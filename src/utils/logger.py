import logging

from config import settings

logging.basicConfig(
    filename=f"{settings.PROJECT_PATH}/logs/pipeline.log",
    encoding="utf-8",
    filemode="a",
    level=logging.DEBUG,
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)
if settings.ENVIRONMENT == "dev":
    logger.setLevel("DEBUG")
