class Menu:

    @staticmethod
    def display_category(id, name):
        print("|| {} ||  {}".format(id, name))

    @staticmethod
    def display_product(id, name):
        print("|| {} ||  {}".format(id, name))

    @staticmethod
    def main_menu(text_menu, separator, line_length):

        print(separator * line_length)
        print(text_menu.center(line_length))
        print(separator * line_length)
        print("")
        print("Sélectionner une action.")
        print("")
        print("|| 0 ||  Quitter le programme.")
        print("|| 1 ||  Quel aliment souhaitez-vous remplacer ?")
        print("|| 2 ||  Retrouver mes aliments substitués.")

    @staticmethod
    def category_menu(text_menu, separator, line_length):

        print(separator * line_length)
        print(text_menu.center(line_length))
        print(separator * line_length)
        print("")
        print("Sélectionner une catégorie.")
        print("")
        print("|| 0 ||  Retourner au menu principale.")

    @staticmethod
    def product_menu(text_menu, separator, line_length):

        print(separator * line_length)
        print(text_menu.center(line_length))
        print(separator * line_length)
        print("")
        print("Sélectionner un aliment.")
        print("")
        print("|| 0 ||  Retourner au menu principale.")

    @staticmethod
    def substitute_menu(text_menu, separator, line_length):

        print(separator * line_length)
        print(text_menu.center(line_length))
        print(separator * line_length)
        print("")
        print("Voici l'aliment proposé.")
        print("")
        print("|| 0 ||  Retour au memu principal.")
        print("|| 1 ||  Enregistrer l'aliment de substitution.")
