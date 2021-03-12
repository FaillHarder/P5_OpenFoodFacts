import mysql.connector



cnx = mysql.connector.connect(user='root',
                            password='test',
                            host='localhost',
                            database='alimentation')
cursor = cnx.cursor()


add_product = ("INSERT INTO product"
        "(name, nutriscore, barcode, link)"
        "VALUES (%s, %s, %s, %s)")

add_category = ("INSERT INTO category"
                "(name)"
                "VALUES (%s)")

add_product_category = ("INSERT INTO product_category"
                        "(id_category, id_product)"
                        "VALUES (%s, %s)")

add_product_store = ("INSERT INTO product_store"
                        "(id_product, id_store)"
                        "VALUES (%s, %s)")