from category import Category
from constants import CATEGORIES, STORES_DICT
from controller import Controller
from get_product_from_api import load_data
from store import Store
from product import Product


def main():

    product_list = load_data(STORES_DICT, CATEGORIES, 1, 200)
    Category.add_in_database(CATEGORIES)
    Store.add_in_database(STORES_DICT)
    Product.add_product_in_database(product_list)
    Controller.selection()


if __name__ == "__main__":
    main()
