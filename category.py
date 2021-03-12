from mysql_code import cnx, cursor



class Category:

    def __init__(self):
        pass


    @staticmethod
    def add_in_database(categories):

        for req in [f"INSERT INTO category (name) VALUES ('{categorie}')" for categorie in categories]:
            cursor.execute(req)
        cnx.commit()
