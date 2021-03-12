from mysql_code import cnx, cursor


class Store:
    
    def __init__(self):
        
        self.stores_liste = []


    def add_list(self, store, stores_liste):

        self.store = store
        self.stores_liste = stores_liste

        self.stores_liste.extend(self.store.lower().split(","))


    @staticmethod
    def stores_cleaner(stores_liste, dict_shop):

        result = set()
        for store in stores_liste:
            for key, value in dict_shop.items():
                if store.strip() in value:
                    result.add(key)
                    break
        return result


    @staticmethod
    def add(stores_liste):

        for req in [f"INSERT INTO store (name) VALUES ('{store}')" for store in stores_liste]:
            cursor.execute(req)
        cnx.commit()