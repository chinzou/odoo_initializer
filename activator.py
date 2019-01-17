import logging

from .utils.config_loader import config_loader
from .models.drug_loader import DrugLoader

# _logger = logging.getLogger(__name__)
#
# config = config_loader()
# loader = DrugLoader()
# config_path = config.config_path
# files = config.get_concept_files()
# _logger.info(files)
# _logger.info(loader.model_name)
# for file in files:
# result = loader.load(BaseModel="product.template", fields=["id", "active", "type", "lst_price", "name",
# "price"], data=file)
#  result = loader.load_file(file)
# _logger.info(result)
#
# _logger.info(config_path)
# _logger.info(get_product_header())
# _logger.info("done")
