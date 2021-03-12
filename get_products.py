import requests



def get_products_from_api(page, category_name, page_size=20):

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
        "page": page
        }

    r = requests.get(url, params)
    reponse = r.json()
    return reponse["products"]


