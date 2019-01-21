import logging
import os
from pathlib import Path

import odoo.tools.config

_logger = logging.getLogger(__name__)


class ConfigLoader:
    @property
    def config_path(self):
        config_path = odoo.tools.config["openmrs_initializer_path"]
        if not config_path:
            _logger.error("Initializer config path is not set")
        return config_path

    def get_files(self, folder, allowed_extensions):
        import_files = []
        if not self.config_path:
            raise ValueError("Invalid config path")
        path = os.path.join(self.config_path, folder)
        _logger.info("path:" + path)
        for root, dirs, files in os.walk(path):
            for file in files:
                ext = Path(file).suffix
                if str(ext).lower() in allowed_extensions:
                    import_files.append(file)
        return import_files


config_loader = ConfigLoader()
