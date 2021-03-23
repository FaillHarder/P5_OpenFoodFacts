class Menu:

    @staticmethod
    def display_liste(a, b):

        print("|| {} ||  {}".format(a, b))

    @staticmethod
    def display_substitute(key, value):

        print("{} : {}".format(key, value))

    @staticmethod
    def display_favorite(name, nutri, link):

        print("Nom du produit : {}, Valeur nutritionnel : {}, Lien : {}".format(name, nutri, link))

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
    def substitute(text_menu, separator, line_length):

        print(separator * line_length)
        print(text_menu.center(line_length))
        print(separator * line_length)
        print("")
        print("Voici l'aliment de substitution proposé.")
        print("")
        print("|| 0 ||  Retour au memu principal.")
        print("|| 1 ||  Enregistrer l'aliment de substitution.")
        print("")

    @staticmethod
    def substitute_menu(text_menu, separator, line_length):

        print(separator * line_length)
        print(text_menu.center(line_length))
        print(separator * line_length)
        print("")
        print("Voici vos aliments de substitution sauvegardés.")
        print("")
        print("|| 0 ||  Retour au memu principal.")
        print("|| 1 ||  Quitter le programme.")

    @staticmethod
    def no_substitute(text_menu, separator, line_length):

        print(separator * line_length)
        print(text_menu.center(line_length))
        print(separator * line_length)
        print("")
        print("L'alliment que vous avez sélectionné dispose déjà du meilleur score nutritionnel.")
        print("")
        print("")
        print("Sélectionner une action.")
        print("")
        print("|| 0 ||  Retour au memu principal.")
        print("|| 1 ||  Quitter le programme.")

    @staticmethod
    def registered_product():

        print("")
        print("Votre produit à bien été enregistré.")
        print("")
        print("|| 0 ||  Retour au memu principal.")
        print("|| 1 ||  Quitter le programme.")

