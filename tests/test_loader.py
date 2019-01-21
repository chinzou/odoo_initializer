from odoo.tests import BaseCase, logging
from odoo.tools.config import config

from src.models.drug_loader import DrugLoader
from src.utils import config_loader

_logger = logging.getLogger(__name__)


class TestOpenmrsLoader(BaseCase):
    def test_drug_loader(self):

        configs = config_loader
        loader = DrugLoader()
        config_path = configs.config_path
        _logger.info(loader.model_name)
        _logger.info(config_path)

    def test_get_config_path(self):
        var = config.config_file
        config.addons_data_dir
        _logger.info(var)
