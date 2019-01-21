import logging
import os

# from odoo.addons.base_import.models.base_import import Import
from odoo import models

from ..utils import config_loader

_logger = logging.getLogger(__name__)


class BaseModelImporter(models.BaseModel):

    model_name = None
    _inherit = model_name

    allowed_file_extensions = [".csv"]
    mapping = None
    folder = None

    def load_files(self, relevant_folder):
        return config_loader.get_files(
            relevant_folder, allowed_extensions=self.allowed_file_extensions
        )

    def load_file(self, file):
        _logger.info(self.model_name)

        import_wizard = self.env["base_import.import"].create(
            {"res_model": self.model_name, "file": file, "file_type": "text/csv"}
        )
        _logger.info(import_wizard)
        result = import_wizard.parse_preview(
            {"quoting": '"', "separator": ",", "headers": True}
        )
        _logger.info(result)
        return result

    def load(self):
        _logger.info("file loading")
        for file_ in self.load_files(self.folder):
            _logger.info("file loaded")
            result = self.load_file(file_)
