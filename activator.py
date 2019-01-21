import logging

from .src.utils import config_loader
from .src.models import DrugLoader

import erppeek

_logger = logging.getLogger(__name__)

registered_loader = [DrugLoader]


for loader_class in registered_loader:
    loader = loader_class()
    loader.load()

_logger.info("done")
