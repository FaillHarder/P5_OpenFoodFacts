import requests
import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='root',
                                password='test',
                                host='localhost',
                                database='alimentation')
    cursor = cnx.cursor()


    add_product = ("INSERT INTO product"
            "(name, nutriscore, barcode, link)"
            "VALUES (%s, %s, %s, %s)")

    def get_product():
        url = "https://fr.openfoodfacts.org/cgi/search.pl"
        params = {"search_simple": 1,
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "sort_by": "Product name",
            "page_size": 50,
            "json": 1
            }

        r = requests.get(url=url, params=params)
        reponse = r.json()
        products = reponse["products"]
        
        for product in products:
            name = product.get("product_name_fr")
            nutriscore = product.get('nutrition_grade_fr')
            barcode = product.get('id')
            link = product.get('url')
            data_product = (name, nutriscore, barcode, link)
            cursor.execute(add_product, data_product)
        cnx.commit()
        cursor.close()
    get_product()


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()





