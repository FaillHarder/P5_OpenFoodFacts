class Menu:

    @staticmethod
    def display_menu(text_menu, separator, line_length):

        print(separator * line_length)
        print(text_menu.center(line_length))
        print(separator * line_length)
        print("")

    @staticmethod
    def display_menu_selection(menu_selection):

        for value in menu_selection.values():
            print(value)

    @staticmethod
    def display_liste(a, b):

        print("|| {} ||  {}".format(a, b))

    @staticmethod
    def display_substitute(key, value):

        print("{} : {}".format(key, value))

    @staticmethod
    def display_favorite(name, nutri, link):

        print("Nom du produit : {},".format(name))
        print("Valeur nutritionnelle : {},".format(nutri.title()))
        print("Lien : {}".format(link))
        print("")
