from category import Category
from constants import CATEGORIES, DICT_SHOP
from get_products import get_products_from_api
from product import Product
from store import Store


stores_list = []
def load_data(categories):

    number_of_product = 0
    page = 1

    while number_of_product < 50:

        products = get_products_from_api(page, categories)

        for product in products:
            product_name = product.get("product_name_fr")
            barcode = product.get("id")
            nutriscore = product.get("nutriscore_grade")
            link = product.get("url")
            stores = product.get("stores")
            if not product_name:
                break
            elif len(product_name) > 80:
                break
            elif not nutriscore:
                break
            elif not link:
                break
            elif not stores:
                break
            else:
                Product.add(Product, product_name, barcode, nutriscore, link)
                Store.add_list(Store, stores, stores_list)            
                number_of_product += 1
        page += 1

    
for category in CATEGORIES:
    load_data(category)

store_set = Store.stores_cleaner(stores_list, DICT_SHOP)
Store.add(store_set)
Category.add(CATEGORIES)