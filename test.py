from constants import (
                        MAIN_MENU, SEPARATOR,
                        CATEGORY_MENU, LINE_LENGTH,
                        PRODUCT_MENU, SUBSTITUTE_MENU
                        )
from view import Menu
from mysql_code import cursor, get_category, get_product_by_category, get_product_substitute


def product(get_product_by_category, user_choice):

    cursor.execute(get_product_by_category.format(user_choice))
    products = cursor.fetchall()
    i = 1
    for id, name in products:
        Menu.display_product(i, name)
        i += 1





def sub():

    liste = []
    cursor.execute(get_product_substitute)
    substitute = cursor.fetchall()
    for name, barcode, nutri, link, store in substitute:
        print(name)
sub()