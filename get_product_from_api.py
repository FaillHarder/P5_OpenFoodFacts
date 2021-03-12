import requests


def load_data(category_name, page_number, page_size=20):

    
    url = "https://fr.openfoodfacts.org/cgi/search.pl"
    params = {
        "action": "process",
        "tagtype_0": "categories",
        "tag_contains_0": "contains",
        "tag_0": category_name,
        "tag_1": "A",
        "json": "true",
        "fields": "product_name_fr,id,stores,nutriscore_grade,url",
        "page_size": page_size,
        "page": page_number
        }

    r = requests.get(url, params)
    reponse = r.json()
    products = reponse["products"]

    products_list = []
    barcode_list = []

    for product in products:
        product_name = product.get("product_name_fr")
        barcode = product.get("id")
        nutriscore = product.get("nutriscore_grade")
        link = product.get("url")
        stores = product.get("stores")
        if not product_name or len(product_name) > 80 or not nutriscore or not link or not stores:
            continue
        else:
            products_list.append({
                "product_name": product_name.title(),
                "barcode": barcode,
                "nutriscore": nutriscore,
                "link": link,
                "category": category_name.title(),
                "stores": stores.split(",")
                })

    return products_list

a = load_data("Pizzas", 1, 100)
for liste in a:
    print(liste["stores"])
print("La liste contient {} éléments".format(len(a)))