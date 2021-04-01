from mysql_code import cnx, cursor


class Category:

    def __init__(self):
        pass

    @staticmethod
    def add_in_database(categories):
        """Function taking as parameter the category list.
        Add each category to the category mysql table"""

        for req in [
            f"INSERT INTO category (name) VALUES ('{categorie}')"
            for categorie in categories
        ]:
            cursor.execute(req)
        cnx.commit()
