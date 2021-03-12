from category import Category
from constants import CATEGORIES, STORES_DICT
from get_product_from_api import load_data
from store import Store
from mysql_code import (cnx, cursor, add_product,
                        add_product_category,
                        add_product_store,
                        sql_select_id,
                        sql_select_las_product_id)


pizza = load_data(STORES_DICT ,"Pizzas", 1, 200)
biscuits = load_data(STORES_DICT, "Biscuits", 1, 200)
petit_dejeuner = load_data(STORES_DICT, "Petit-déjeuners", 1, 200)


Category.add_in_database(CATEGORIES)
Store.add_in_database(STORES_DICT)


def add_product_in_bdd(products_list, name):

    for product in products_list:
        data = [product["product_name"], product["nutriscore"], product["barcode"], product["link"]]
        cursor.execute(add_product, data)
        id_product = sql_select_las_product_id()
        id_category = sql_select_id("category", name)
        values = [id_category, id_product]
        cursor.execute(add_product_category, values)
        for store in product["stores"]:
            id_product = sql_select_las_product_id()
            id_store = sql_select_id("store", store)
            values = [id_product, id_store]
            cursor.execute(add_product_store, values)
                    
    cnx.commit()

add_product_in_bdd(pizza, "Pizzas")
add_product_in_bdd(biscuits, "Biscuits")
add_product_in_bdd(petit_dejeuner, "Petit-déjeuners")








