import mysql.connector


cnx = mysql.connector.connect(
                            user='root',
                            password='test',
                            host='localhost',
                            database='alimentation'
                            )
cursor = cnx.cursor()

add_product = (
                "INSERT INTO product"
                "(name, nutriscore, barcode, link)"
                "VALUES (%s, %s, %s, %s)"
                )

add_category = (
                "INSERT INTO category"
                "(name)"
                "VALUES (%s)"
                )

add_product_category = (
                        "INSERT INTO product_category"
                        "(id_category, id_product)"
                        "VALUES (%s, %s)"
                        )

add_product_store = (
                    "INSERT INTO product_store"
                    "(id_product, id_store)"
                    "VALUES (%s, %s)"
                    )

get_category = ("SELECT * FROM category ORDER BY id")

get_product = ("SELECT id, name FROM product ORDER BY id")

get_product_by_category = (
                            "SELECT name, nutriscore FROM product "
                            "INNER JOIN product_category "
                            "ON product.id = product_category.id_product "
                            "WHERE product_category.id_category = '{}';"
                            )

get_substitute = (
            "SELECT product.id, product.name, nutriscore, link, store.name "
            "FROM product "
            "INNER JOIN product_store "
            "ON product.id = product_store.id_product "
            "INNER JOIN store "
            "ON store.id = product_store.id_store "
            "INNER JOIN product_category "
            "ON product.id = product_category.id_product "
            "WHERE product.nutriscore < '{}' "
            "AND product_category.id_category = {};"
                )

add_into_favorite = (
                    "UPDATE product "
                    "SET favorite = 1 "
                    "WHERE product.id = {};"
                    )

get_favorite = (
                "SELECT product.name, nutriscore, link "
                "FROM product "
                "WHERE favorite = 1;"
                )


def sql_select_last_product_id():

    req = "SELECT max(id) FROM product;"
    cursor.execute(req)
    result = cursor.fetchone()
    return result[0]


def sql_select_id(table, name):

    req = "SELECT id FROM {} WHERE name='{}';".format(table, name)
    cursor.execute(req)
    result = cursor.fetchone()
    return result[0]
