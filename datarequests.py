import requests
import mysql.connector
from mysql.connector import errorcode
from mysql_code import cnx, cursor


def main():

    products = get_products_from_api("Snacks", 100)
    shops = set()
    for prod in products:
        if "stores" in prod:
            for store in prod["stores"].split(","):
                if store:
                    shops.add(store.lower())
    print(shops)
        
    
    cnx = mysql.connector.connect(user='root',
                                password='test',
                                host='localhost',
                                database='alimentation')
    cursor = cnx.cursor()
    for req in [f"INSERT INTO store (name) VALUES ('{shop}')" for shop in shops]:
        cursor.execute(req)
    cnx.commit()






def get_products_from_api(search_terms, page_size):
    url = "https://fr.openfoodfacts.org/cgi/search.pl"
    params = {"search_simple": 1,
        "action": "process",
        "search_terms": search_terms,
        "tag_contains_0": "contains",
        "sort_by": "Product name",
        "fields": "categories,product_name_fr,stores,nutriscore_grade,url",
        "page_size": page_size,
        "json": 1
        }

    r = requests.get(url=url, params=params)
    reponse = r.json()
    return reponse["products"]
    

if __name__ == "__main__":
    main()

