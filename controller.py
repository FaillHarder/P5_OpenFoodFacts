from constants import (
                        MAIN_MENU, SEPARATOR,
                        CATEGORY_MENU, LINE_LENGTH,
                        PRODUCT_MENU, SUBSTITUTE_MENU
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
        for id, name, barcode, nutriscore, link, store in substitute:
            substitute_list.append({
                                    "id": id,
                                    "Nom du produit": name,
                                    "Code-barre": barcode,
                                    "Score nutritionnel": nutriscore,
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
            Menu.display_favorite(name, nutriscore, link)

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
                    Menu.product_menu(PRODUCT_MENU, SEPARATOR, LINE_LENGTH)
                    substitute = cls.product_to_substitute(
                        get_product_by_category, user_choice
                        )
                    state = "substitute"

            elif state == "substitute":
                Menu.substitute(SUBSTITUTE_MENU, SEPARATOR, LINE_LENGTH)
                try:
                    sub = choice(substitute)
                    for key, value in sub.items():
                        Menu.display_substitute(key, value)
                    user_choice = cls.choice_number(0, 1)
                    if user_choice == 0:
                        state = "main_menu"
                    elif user_choice == 1:
                        cls.save_substitute(add_into_favorite, sub["id"])
                        Menu.registered_product()
                        choice_number = cls.choice_number(0, 1)
                        if choice_number == 0:
                            state = "main_menu"
                        elif choice_number == 1:
                            state = "quit"
                except IndexError:
                    Menu.no_substitute(SUBSTITUTE_MENU, SEPARATOR, LINE_LENGTH)
                    user_choice = cls.choice_number(0, 1)
                    if user_choice == 0:
                        state = "main_menu"
                    elif user_choice == 1:
                        state = "quit"

            elif state == "substitute_menu":
                Menu.substitute_menu(SUBSTITUTE_MENU, SEPARATOR, LINE_LENGTH)
                cls.get_product_favorite(get_favorite)
                user_choice = cls.choice_number(0, 1)
                if user_choice == 0:
                    state = "main_menu"
                elif user_choice == 1:
                    print("vous avez enregistré l'aliment de substitution.")
                    state = "main_menu"
