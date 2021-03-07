import mysql.connector



cnx = mysql.connector.connect(user='root',
                            password='test',
                            host='localhost',
                            database='alimentation')
cursor = cnx.cursor()


add_product = ("INSERT INTO product"
        "(name, nutriscore, barcode, link)"
        "VALUES (%s, %s, %s, %s)")

