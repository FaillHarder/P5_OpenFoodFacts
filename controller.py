from constants import (
                        MAIN_MENU, SEPARATOR,
                        CATEGORY_MENU, LINE_LENGTH,
                        PRODUCT_MENU, SUBSTITUTE_MENU
                        )
from view import Menu
from mysql_code import cursor, get_category, get_product_by_category


class Controller:

    @staticmethod
    def choice_number(min, max):

        while True:

            try:
                x = int(input("Entrez votre sélection :"))
                if x >= min and x <= max:
                    return x
                else:
                    print("Vous devez entrer un nombre compris entre {} et {}".format(min, max))
            except ValueError:
                print("Vous devez entrer un nombre compris entre {} et {}".format(min, max))

    @classmethod
    def category(cls, get_category):

        cursor.execute(get_category)
        category = cursor.fetchall()
        last_id = 0
        for id, name in category:
            Menu.display_category(id, name)
            last_id += 1

        user_choice = cls.choice_number(0, last_id)
        return user_choice

    @classmethod
    def product(cls, get_product_by_category, user_choice):

        cursor.execute(get_product_by_category.format(user_choice))
        products = cursor.fetchall()
        i = 1
        for id, name in products:
            Menu.display_product(i, name)
            i += 1
        cls.choice_number(0, i)

    @classmethod
    def selection(cls):

        state = "main_menu"
        while state != "quit":

            if state == "main_menu":
                Menu.main_menu(MAIN_MENU, SEPARATOR, LINE_LENGTH)
                user_choice = cls.choice_number(0, 2)
                if user_choice == 0:
                    state = "quit"
                elif user_choice == 1:
                    state = "category_menu"
                elif user_choice == 2:
                    state = "substitute_menu"

            elif state == "category_menu":
                Menu.category_menu(CATEGORY_MENU, SEPARATOR, LINE_LENGTH)
                user_choice = cls.category(get_category)
                if user_choice == 0:
                    state = "main_menu"
                elif user_choice > 0:
                    state = "product"
                    Menu.product_menu(PRODUCT_MENU, SEPARATOR, LINE_LENGTH)
                    cls.product(get_product_by_category, user_choice)

            # elif state == "product":
            #     Menu.product_menu(PRODUCT_MENU, SEPARATOR, LINE_LENGTH)
            #     user_choice = cls.choice_number(0, 5)
            #     if user_choice == 0:
            #         state = "main_menu"

            elif state == "substitute_menu":
                Menu.substitute_menu(SUBSTITUTE_MENU, SEPARATOR, LINE_LENGTH)
                user_choice = cls.choice_number(0, 1)
                if user_choice == 0:
                    state = "main_menu"
                elif user_choice == 1:
                    print("vous avez enregistré l'aliment de substitution.")
                    state = "main_menu"


Controller.selection()
