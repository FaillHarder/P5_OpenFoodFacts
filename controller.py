from constants import (
                    MAIN_MENU, SEPARATOR,
                    CATEGORY_MENU, LINE_LENGTH,
                    PRODUCT_MENU, SUBSTITUTE_MENU,
                    MAIN_SELECTION, CATEGORY_SELECTION,
                    PRODUCT_SELECTION, SUBSTITUTE_SAVE_SELECTION,
                    PROPOSED_SUBSTITUTE,
                    SUBSTITUTE_MENU_SELECTION,
                    NO_SUBSTITUTE_SELECTION, REGISTERED_SELECTION
)
from mysql_code import (
                    cnx, cursor, get_category,
                    get_product_by_category,
                    get_substitute,
                    add_into_favorite,
                    get_favorite
)
from view import Menu

import os
from random import choice


class Controller:

    @staticmethod
    def clear():
        """Method to clean the terminal"""
        os.system('cls')

    @staticmethod
    def choice_number(min, max):
        """Method input. Allows the user to make a selection"""

        while True:

            try:
                x = int(input("Entrez votre sélection :"))
                message = "Sélectionner un nombre entre {} et {}"
                if x >= min and x <= max:
                    return x
                else:
                    print(message.format(min, max))
            except ValueError:
                print(message.format(min, max))

    @classmethod
    def category(cls, request_mysql):
        """Method taking as argument the mysql request get_category.
        She display a category list find in mysql category table,
        calls the choice méthode and return the chosen number"""

        cursor.execute(request_mysql)
        category = cursor.fetchall()
        last_id = 0
        for id, name in category:
            Menu.display_liste(id, name)
            last_id += 1

        category_choice = cls.choice_number(0, last_id)
        return category_choice

    @classmethod
    def product_to_substitute(cls, request_mysql, category_choice):
        """Method taking the mysql request get_product_by_category
        and the number returned by Controller.category() as arguments.
        She displays a product list from mysql product table, adds
        the nutriscore of each product in id_product dictionary and
        calls the choice méthode. Return product_choice (nutriscore
        of the selected product) and id_category (product category)"""

        id_product = {}
        id_category = category_choice
        cursor.execute(request_mysql.format(category_choice))
        products = cursor.fetchall()
        i = 0
        for name, nutriscore in products:
            i += 1
            Menu.display_liste(i, name)
            id_product[i] = nutriscore

        choice = cls.choice_number(1, i)
        product_choice = id_product[choice]

        return product_choice, id_category

    @staticmethod
    def substitute(product_nutriscore, id_category):
        """Method taking as arguments the return of product_to_substitute.
        She executes the request mysql get_substitute to add to the
        substitute_list all products less than product_nutriscore
        and return substitute_list."""

        substitute_list = []
        cursor.execute(
            get_substitute.format(product_nutriscore, id_category)
            )
        substitute = cursor.fetchall()
        for id, name, nutriscore, link, store in substitute:
            substitute_list.append({
                                    "id": id,
                                    "Nom du produit": name,
                                    "Score nutritionnel": nutriscore.title(),
                                    "Lien": link,
                                    "Vendu à": store
                                    })
        return substitute_list

    @staticmethod
    def save_substitute(request_mysql, id_product):
        """Method used to save a product as a favored by
        taking add_into_favorite and id_product as arguments"""

        cursor.execute(request_mysql.format(id_product))
        cnx.commit()

    @staticmethod
    def get_product_favorite(request_mysql):
        """Method taking as argument the mysql request
        get_favorite and display the favored products"""

        cursor.execute(request_mysql)
        favorite = cursor.fetchall()
        if not favorite:
            print("Aucun aliment de substitution n'est encore enregisté.")
        else:
            for name, nutriscore, link in favorite:
                Menu.display_favorite(name, nutriscore.title(), link)

    @classmethod
    def selection(cls):
        """Méthod used to launch the program"""

        state = "main_menu"
        while state != "quit":

            cls.clear()
            if state == "main_menu":
                Menu.display_menu(MAIN_MENU, SEPARATOR, LINE_LENGTH)
                Menu.display_menu_selection(MAIN_SELECTION)

            elif state == "category_menu":
                Menu.display_menu(CATEGORY_MENU, SEPARATOR, LINE_LENGTH)
                Menu.display_menu_selection(CATEGORY_SELECTION)

            elif state == "substitute":
                Menu.display_menu(PROPOSED_SUBSTITUTE, SEPARATOR, LINE_LENGTH)

            elif state == "substitute_menu":
                Menu.display_menu(SUBSTITUTE_MENU, SEPARATOR, LINE_LENGTH)
                cls.get_product_favorite(get_favorite)
                Menu.display_menu_selection(SUBSTITUTE_MENU_SELECTION)

            if state == "main_menu":
                user_choice = cls.choice_number(0, 2)
                if user_choice == 0:
                    state = "quit"
                elif user_choice == 1:
                    state = "category_menu"
                elif user_choice == 2:
                    state = "substitute_menu"

            elif state == "category_menu":
                user_choice = cls.category(get_category)
                if user_choice == 0:
                    state = "main_menu"
                elif user_choice > 0:
                    Menu.display_menu(PRODUCT_MENU, SEPARATOR, LINE_LENGTH)
                    Menu.display_menu_selection(PRODUCT_SELECTION)
                    substitute = cls.product_to_substitute(
                        get_product_by_category, user_choice
                        )
                    state = "substitute"

            elif state == "substitute":
                substitute_list = cls.substitute(substitute[0], substitute[1])

                try:
                    sub = choice(substitute_list)
                    for key, value in sub.items():
                        Menu.display_substitute(key, value)
                    Menu.display_menu_selection(SUBSTITUTE_SAVE_SELECTION)
                    user_choice = cls.choice_number(0, 1)
                    if user_choice == 0:
                        state = "main_menu"
                    elif user_choice == 1:
                        cls.save_substitute(add_into_favorite, sub["id"])
                        cls.clear()
                        Menu.display_menu_selection(REGISTERED_SELECTION)
                        choice_number = cls.choice_number(0, 1)
                        if choice_number == 0:
                            state = "main_menu"
                        elif choice_number == 1:
                            state = "quit"

                except IndexError:
                    Menu.display_menu_selection(NO_SUBSTITUTE_SELECTION)
                    user_choice = cls.choice_number(0, 1)
                    if user_choice == 0:
                        state = "main_menu"
                    elif user_choice == 1:
                        state = "quit"

            elif state == "substitute_menu":
                user_choice = cls.choice_number(0, 1)
                if user_choice == 0:
                    state = "main_menu"
                elif user_choice == 1:
                    state = "quit"
