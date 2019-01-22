import csv
import logging

from odoo import api, fields, models

from .base_loader import BaseModelImporter

_logger = logging.getLogger(__name__)


class DrugLoader(BaseModelImporter):

    model_name = "product.template"
    mapping = {"Fully specified name:en": "name", "Data class": "type"}
    folder = "concepts"

