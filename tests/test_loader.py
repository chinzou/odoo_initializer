from odoo.tests import TransactionCase, logging
from  odoo.tools.config import config


_logger = logging.getLogger(__name__)


class TestOpenmrsLoader(TransactionCase):

    # def test_drug_loader(self):
    #
    #     configs = config_loader()
    #     loader = DrugLoader()
    #     config_path = configs.config_path
    #     files = configs.get_concept_files()
    #     _logger.info(files)
    #     _logger.info(loader.model_name)

    def test_get_config_path(self):
        var = config.config_file
        config.addons_data_dir
        _logger.info(var)
