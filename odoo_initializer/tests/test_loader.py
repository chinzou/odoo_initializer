from odoo.tests import BaseCase, logging
from odoo.tools.config import config


from models.drug_loader import DrugLoader
from utils import config_loader

_logger = logging.getLogger(__name__)


class TestOpenmrsLoader(BaseCase):
    def test_drug_loader(self):

        configs = config_loader
        loader = DrugLoader()
        config_path = configs.config_path
        loader.load_()
        _logger.info(loader.model_name)
        _logger.info(config_path)

    def test_my_module(self):
        registered_loader = [DrugLoader]

        for loader_class in registered_loader:
            loader = loader_class()
            loader.load_()

    def test_get_config_path(self):
        var = config.config_file
        config.addons_data_dir
        _logger.info(var)
