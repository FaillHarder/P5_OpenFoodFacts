from mysql_code import cnx, cursor

add_product = ("INSERT INTO product"
        "(name, nutriscore, barcode, link)"
        "VALUES ((SELECT id FROM category WHERE name = 'Pizza'), %s, %s, %s, %s)")





class Mysql_shortcut():

        @staticmethod
        def sql_select_las_product_id():
                req = "SELECT max(id) FROM product;"
                cursor.execute(req)
                result = cursor.fetchone()
                return result[0]


        @staticmethod
        def sql_select_id(table, name):
                req = "SELECT id FROM {} WHERE name='{}';".format(table, name)
                cursor.execute(req)
                result = cursor.fetchone()
                return result[0]


