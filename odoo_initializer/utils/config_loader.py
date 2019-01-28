import csv
import logging
import os
from pathlib import Path
import hashlib
import odoo.tools.config
import odoorpc

_logger = logging.getLogger(__name__)


class ConfigLoader:
    def __init__(self):
        self._host = "localhost"
        self._port = odoo.tools.config["http_port"]
        self._username = "admin"
        try:
            self._password = odoo.tools.config["admin_password"]
        except:
            self._password = "admin"
        try:
            self._db_name = odoo.tools.config["db_name"]
        except:
            pass
        self.odoo_ = self._authenticate()

    def get_config_path(self, config_source):
        config_source = config_source.lower()
        assert config_source in ["odoo", "openmrs"]

        path = (
            "openmrs_initializer_path"
            if config_source == "openmrs"
            else "odoo_initializer_path"
        )
        config_path = odoo.tools.config[path]
        if not config_path:
            _logger.error("Initializer config path is not set")
        return config_path

    def _authenticate(self):
        try:
            rpc = odoorpc.ODOO(self._host, port=self._port)
        except:
            raise Exception("odoo server not available!")
        if not odoo.tools.config["db_name"]:
            self._db_name = rpc.db.list()[0]
        rpc.login("bahmni", "chine.zoheir@gmail.com", "zou4ever")
        return rpc

    def get_files(self, config_source, folder, allowed_extensions):
        import_files = []
        if not self.get_config_path(config_source):
            _logger.info(ValueError("Invalid config path"))
            return []
        path = os.path.join(self.get_config_path(config_source), folder)
        _logger.info("path:" + path)
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(path, file)
                if self.file_already_processed(file_path):
                    _logger.info("Skipping already processed file:", file)
                    continue

                ext = Path(file).suffix
                if str(ext).lower() in allowed_extensions:
                    with open(os.path.join(path, file), "r") as file_data:
                        extracted_csv = csv.DictReader(file_data)
                        csv_dict = []
                        for row in extracted_csv:
                            csv_dict.append(row)
                        import_files.append(csv_dict)
        return import_files

    def file_already_processed(self, file_: str) -> bool:
        checksum_path = "%s%s" % (file_, ".checksum")
        md5 = self.md5(file_)
        old_md5 = None
        if os.path.exists(checksum_path):
            with open(checksum_path, "rw") as f:
                old_md5 = f.read()
                if old_md5 != md5:
                    f.write(md5)
            return old_md5 == md5

        with open(checksum_path, "w") as f:
            f.write(md5)
        return False

    def md5(self, fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()


config_loader = ConfigLoader()
