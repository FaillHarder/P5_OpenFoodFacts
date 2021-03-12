from teste import Mysql
from category import Category
from constants import CATEGORIES, STORES_DICT
from get_product_from_api import load_data
from store import Store
from mysql_code import cnx, cursor, add_product, add_product_category, add_product_store


pizza = load_data("Pizzas", 1, 200)
biscuits = load_data("Biscuits", 1, 20)
petit_dejeuner = load_data("Petit-déjeuners", 1, 20)


Category.add(CATEGORIES)
Store.add(STORES_DICT)


def add_product_in_bdd(products_list, name, stores_dict):

    for product in products_list:
        data = [product["product_name"], product["nutriscore"], product["barcode"], product["link"]]
        cursor.execute(add_product, data)
        id_product = Mysql.sql_select_las_product_id()
        id_category = Mysql.sql_select_id("category", name)
        values = [id_category, id_product]
        cursor.execute(add_product_category, values)
        for store in product["stores"]:
            for key, value in stores_dict.items():
                if store.lower() in value:
                    id_product = Mysql.sql_select_las_product_id()
                    id_store = Mysql.sql_select_id("store", key)
                    values = [id_product, id_store]
                    cursor.execute(add_product_store, values)
                    
    cnx.commit()

add_product_in_bdd(pizza, "Pizzas", STORES_DICT)
# add_product_in_bdd(biscuits, "Biscuits", STORES_DICT)
# add_product_in_bdd(petit_dejeuner, "Petit-déjeuners", STORES_DICT)








