from odoo import models
from odoo.addons.base_import.models.base_import import Import


from ..utils.config_loader import config_loader
from ..utils.initz_mapper import get_product_header


class BaseLoader(Import):

    def __init__(self):
        super.__init__(self)
        configurator = config_loader()
        self.files = configurator.get_concept_files()
        self.model_name = self._get_model_name()

    def _get_model_name(self):
        raise NotImplementedError("The method not implemented")

    def load_file(self, file):
        header = get_product_header(file.readline())
        # for line in file.nextline():
        #   self.env[self.model_name].create(header, line)
