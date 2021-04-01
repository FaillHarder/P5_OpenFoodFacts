from constants import CATEGORIES, STORES_DICT, PAGE, NB_PRODUCT_BY_CATEGORY
from get_product_from_api import get_data
from models.category import Category
from models.store import Store
from models.product import Product


product_list = get_data(STORES_DICT, CATEGORIES, PAGE, NB_PRODUCT_BY_CATEGORY)
Category.add_in_database(CATEGORIES)
Store.add_in_database(STORES_DICT)
Product.add_product_in_database(product_list)
