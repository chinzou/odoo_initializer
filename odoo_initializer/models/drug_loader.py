import csv
import logging

from odoo import api, fields, models

from .base_loader import BaseModelImporter

_logger = logging.getLogger(__name__)


class DrugLoader(BaseModelImporter):
    update = True
    config_source = "openmrs"
    model_name = "product.template"
    mapping = {"name": "Fully specified name:en", "lst_price": "odoo_price"}
    folder = "concepts"
    filter_ = {}
    identifier = "name"
