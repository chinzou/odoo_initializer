import os

import odoo.tools.config

import logging

_logger = logging.getLogger(__name__)


def _get_config_path():
    config_path = odoo.tools.config['openmrs_initializer_path']
    if not config_path:
        _logger.error("Initializer config path is not set")
    return config_path


class config_loader:

    def __init__(self):
        self.config_path = _get_config_path()

    def get_concept_files(self):
        concept_files = []
        if self.config_path:
            for root, dirs, files in os.walk(self.config_path + "/concepts"):
                for file in files:
                    if file.endswith(".csv"):
                        concept_files.append(file)
        return concept_files

    def get_drug_files(self):
        concept_files = []
        if self.config_path:
            for root, dirs, files in os.walk(self.config_path + "/drugs"):
                for file in files:
                    if file.endswith(".csv"):
                        concept_files.append(file)
        return concept_files

# _logger.info("Here i am in the module")
# directory_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# _logger.info(directory_path.casefold())
# import_file = open(directory_path + "/products.csv", 'r')
# header_file = import_file.readline()
# _logger.info(header_file)
# _logger.info("file read successfully!")
# my_model = models.BaseModel
# my_model.load('product', ['active', 'name'], import_file)
