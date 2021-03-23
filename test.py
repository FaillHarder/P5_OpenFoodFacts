from mysql_code import cnx, cursor, get_favorite



get_favorite = (
                "SELECT product.name, nutriscore, link "
                "FROM product "
                "WHERE favorite = 1;"
                )

def get_product_favorite(mysql_requet):

    sub = cursor.execute(mysql_requet)
    for prod in sub:
        print(prod)

get_product_favorite(get_favorite)