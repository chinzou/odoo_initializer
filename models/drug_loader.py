import logging

from .base_loader import BaseLoader

_logger = logging.getLogger(__name__)


class DrugLoader(BaseLoader):

    def _get_model_name(self):
        return "product.template"

    _name = "product.template"

    def load_file(self, file):
        self.model_name = "product.template"
        _logger.info(self._get_model_name())

        import_wizard = self.env['base_import.import'].create({
            'res_model': self._get_model_name(),
            'file': file,
            'file_type': 'text/csv'
        })

        result = import_wizard.parse_preview({
            'quoting': '"',
            'separator': ',',
            'headers': True,
        })
        return result
