from mysql_code import (cnx, cursor, add_product,
                        add_product_category,
                        add_product_store,
                        sql_select_id,
                        sql_select_last_product_id)


class Product:

    def __init__(self):
        pass

    @staticmethod
    def add_product_in_database(products_list):
        """Function taking as parameter the dictionary list
        returned by get_product_from_api(). Each product is
        added to the product table to then be associated
        with a category and its stores."""

        for product in products_list:
            data = [
                product["product_name"],
                product["nutriscore"],
                product["barcode"],
                product["link"]
                    ]
            cursor.execute(add_product, data)
            id_product = sql_select_last_product_id()
            id_category = sql_select_id("category", product["category"])
            values = [id_category, id_product]
            cursor.execute(add_product_category, values)
            for store in product["stores"]:
                id_product = sql_select_last_product_id()
                id_store = sql_select_id("store", store)
                values = [id_product, id_store]
                cursor.execute(add_product_store, values)
        cnx.commit()
