from category import Category
from constants import CATEGORIES, STORES_DICT
from get_product_from_api import load_data
from store import Store
from add_product_in_database import add_product_in_database


def main():

    product_list = load_data(STORES_DICT, CATEGORIES, 1, 10)
    Category.add_in_database(CATEGORIES)
    Store.add_in_database(STORES_DICT)
    add_product_in_database(product_list)


if __name__ == "__main__":
    main()
