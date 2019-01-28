import logging

import csv

from utils import config_loader

_logger = logging.getLogger(__name__)


class BaseModelImporter:
    model_name = None

    config_source = "odoo"  # ["openmrs, "odoo"]
    update_existing_record = False
    identifier = None
    allowed_file_extensions = [".csv"]  # supported file extensions
    mapping = None
    folder = None
    filter_ = {}

    def load_files(self, relevant_folder):
        return config_loader.get_files(
            self.config_source,
            relevant_folder,
            allowed_extensions=self.allowed_file_extensions,
        )

    def load_file(self, file):

        model = config_loader.odoo_.env[self.model_name]

        for record in file:
            found_ids = model.search([(self.identifier, "=", record[self.identifier])])
            if found_ids and not self.update:
                _logger.info("Skipping record with IDs:", found_ids)
                continue

            if found_ids:
                # TODO: what if there are two IDs found for the same record
                _logger.info("Updating existing records for IDs:", found_ids)
                model.write([found_ids[0]], record)
            else:
                model.create(record)

        return file

    def _mapper(self, file_, mapping={}, filters_={}):
        if not isinstance(filters_, dict):
            filters_ = {}
        mapped_csv = []

        for dict_line in file_:
            row = {}
            for key, value in mapping.items():
                if value in dict_line.keys():
                    row[key] = dict_line.pop(value)

            if not filters_:
                mapped_csv.append(row)

            for filter_key, filter_value in filters_.items():
                if filter_key in row.keys():
                    filter_value = (
                        [filter_value]
                        if not isinstance(filter_value, list)
                        else filter_value
                    )
                    if row[filter_key] in filter_value:
                        mapped_csv.append(row)
        return mapped_csv

    def load_(self):
        _logger.info("file loading")
        for file_ in self.load_files(self.folder):
            mapped_file = self._mapper(file_, self.mapping, self.filter_)

            self.load_file(mapped_file)
