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
from view import Menu
from mysql_code import (
                        cnx, cursor, get_category,
                        get_product_by_category,
                        get_substitute,
                        add_into_favorite,
                        get_favorite
                        )

from random import choice


class Controller:

    @staticmethod
    def choice_number(min, max):

        while True:

            try:
                x = int(input("Entrez votre sélection :"))
                if x >= min and x <= max:
                    return x
                else:
                    print("Sélectionner un nombre entre {} et {}".format(min, max))
            except ValueError:
                print("Sélectionner un nombre entre {} et {}".format(min, max))

    @classmethod
    def category(cls, get_category):

        cursor.execute(get_category)
        category = cursor.fetchall()
        last_id = 0
        for id, name in category:
            Menu.display_liste(id, name)
            last_id += 1

        category_choice = cls.choice_number(0, last_id)
        return category_choice

    @classmethod
    def product_to_substitute(cls, get_product_by_category, category_choice):

        id_product = {}
        id_category = category_choice
        cursor.execute(get_product_by_category.format(category_choice))
        products = cursor.fetchall()
        i = 0
        for id, name, nutriscore in products:
            i += 1
            Menu.display_liste(i, name)
            id_product[i] = nutriscore

        product_choice = cls.choice_number(0, i)

        substitute_list = []
        cursor.execute(get_substitute.format(id_product[product_choice], id_category))
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
    def save_substitute(requete_mysql, id_product):

        cursor.execute(requete_mysql.format(id_product))
        cnx.commit()

    @staticmethod
    def get_product_favorite(requete_mysql):

        cursor.execute(requete_mysql)
        favorite = cursor.fetchall()
        for name, nutriscore, link in favorite:
            Menu.display_favorite(name, nutriscore.title(), link)

    @classmethod
    def selection(cls):

        state = "main_menu"
        while state != "quit":

            if state == "main_menu":
                Menu.display_menu(MAIN_MENU, SEPARATOR, LINE_LENGTH)
                Menu.display_menu_selection(MAIN_SELECTION)
                user_choice = cls.choice_number(0, 2)
                if user_choice == 0:
                    state = "quit"
                elif user_choice == 1:
                    state = "category_menu"
                elif user_choice == 2:
                    state = "substitute_menu"

            elif state == "category_menu":
                Menu.display_menu(CATEGORY_MENU, SEPARATOR, LINE_LENGTH)
                Menu.display_menu_selection(CATEGORY_SELECTION)
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
                Menu.display_menu(PROPOSED_SUBSTITUTE, SEPARATOR, LINE_LENGTH)
                try:
                    sub = choice(substitute)
                    for key, value in sub.items():
                        Menu.display_substitute(key, value)
                    Menu.display_menu_selection(SUBSTITUTE_SAVE_SELECTION)
                    user_choice = cls.choice_number(0, 1)
                    if user_choice == 0:
                        state = "main_menu"
                    elif user_choice == 1:
                        cls.save_substitute(add_into_favorite, sub["id"])
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
                Menu.display_menu(SUBSTITUTE_MENU, SEPARATOR, LINE_LENGTH)
                cls.get_product_favorite(get_favorite)
                Menu.display_menu_selection(SUBSTITUTE_MENU_SELECTION)
                user_choice = cls.choice_number(0, 1)
                if user_choice == 0:
                    state = "main_menu"
                elif user_choice == 1:
                    print("vous avez enregistré l'aliment de substitution.")
                    state = "main_menu"


Controller.selection()
