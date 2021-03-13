import requests


def load_data(stores_dict, category_list, page_number, page_size=20):
    """Function allowing to retrieve data from the OpenFoodFacts API.
    Take as parameters, store dictionary, food category,
    page number and page size. Return a dictionary list"""

    products_list = []

    for category in category_list:
        url = "https://fr.openfoodfacts.org/cgi/search.pl"
        params = {
                "action": "process",
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "tag_0": category,
                "tag_1": "A",
                "json": "true",
                "fields": "product_name_fr,id,stores,nutriscore_grade,url",
                "page_size": page_size,
                "page": page_number
            }

        r = requests.get(url, params)
        reponse = r.json()
        products = (reponse["products"])

        for product in products:
            stores_list = []
            stores_set = set()
            product_name = product.get("product_name_fr")
            barcode = product.get("id")
            nutriscore = product.get("nutriscore_grade")
            link = product.get("url")
            stores = product.get("stores")
            if (
                not product_name or len(product_name) > 80
                or not nutriscore or not link or len(link) > 120 or not stores
                    ):
                continue
            else:
                stores_list = stores.split(",")
                for store in stores_list:
                    # Using the dictionary to clean up the
                    # store list for every product
                    for key, value in stores_dict.items():
                        if store.lower() in value:
                            stores_set.add(key)

                products_list.append({
                    "product_name": product_name.title(),
                    "barcode": barcode,
                    "nutriscore": nutriscore,
                    "link": link,
                    "category": category.title(),
                    "stores": stores_set
                    })

    return products_list
