from get_product_from_api import load_data
from constants import STORES_DICT


pizza = load_data("Pizzas", 1, 200)


def shops_clear(product_list, stores_dict):

    shops = set()
    result = []
    for product in product_list:
        for store in product["stores"]:
            for key, value in stores_dict.items():
                if store in value:
                    shops.add(key)
        result.append({
            product["product_name"],
            product["barcode"],
            product["nutriscore"],
            product["link"],
            product["category"],
            product[shops]
        })       
    return result


pizzas = shops_clear(pizza, STORES_DICT)

for p in pizzas:
    print(p)