from mysql_code import cnx, cursor


class Store:

    def __init__(self):

        pass

    @staticmethod
    def add_in_database(stores_liste):
        """Function taking as parameter the stores dictionary.
        Add each store to the store mysql table"""

        for req in [
            f"INSERT INTO store (name) VALUES ('{store}')"
            for store in stores_liste
                ]:
            cursor.execute(req)
        cnx.commit()
