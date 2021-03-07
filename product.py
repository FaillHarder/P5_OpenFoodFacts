from mysql_code import cnx, cursor, add_product


class Product:

    def __init__(self):
        
        self.product_name = ""   
        self.barcode = ""
        self.nutriscore = ""
        self.link = ""


    def add(self, product_name, barcode, nutriscore, link):

        self.product_name = product_name
        self.barcode = barcode
        self.nutriscore = nutriscore
        self.link = link

        data_product = [self.product_name, self.nutriscore, self.barcode, self.link]

        cursor.execute(add_product, data_product)
        cnx.commit()