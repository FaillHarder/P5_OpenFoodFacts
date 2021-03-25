CATEGORIES = ["Pizzas", "Biscuits", "Petit-déjeuners", "Jambons", "Apéritif"]

STORES_DICT = {
    "Magasin U": [
        'magasins u', 'u', 'supermarché',
        'super u', 'cora intermarche superu'
        ],
    "E.Leclerc": [
        'leclerc', 'e.leclerc', 'e. leclerc',
        'e leclerc', 'carrefour auchan leclerc'
        ],
    "Carrefour": [
        'carrefour city', 'carrefour', 'carrefour market',
        'carrefour auchan', 'carrefour auchan leclerc'
        ],
    "Intermarché": [
        'intermarchė', 'intermarche',
        'cora intermarche superu', 'intermarché'
        ],
    "Casino": ['géant', 'geantcasino', 'casino', 'casino supermarché'],
    "Leader Price": ['leader price'],
    "Auchan": ['carrefour auchan', 'auchan', 'carrefour auchan leclerc'],
    "Spar": ['spar'],
    "Aldi": ['aldi'],
    "Lidl": ['lidl'],
    "Picard": ['picard'],
    "Cora": ['cora'],
    "Franprix": ['franprix'],
    "Dia": ['dia']
}

MAIN_MENU = "MENU PRINCIPAL"
CATEGORY_MENU = "CATEGORIES"
PRODUCT_MENU = "PRODUITS"
PROPOSED_SUBSTITUTE = "ALIMENT DE SUBSTITUTION PROPOSÉ"
SUBSTITUTE_MENU = "ALIMENT DE SUBSTITUTION ENREGISTRÉ"
SEPARATOR = ("#")
LINE_LENGTH = 90

MAIN_SELECTION = {
                    "0": "",
                    "1": "Sélectionnez une action.",
                    "2": "",
                    "3": "|| 0 ||  Quitter le programme.",
                    "4": "|| 1 ||  Quel aliment souhaitez-vous remplacer ?",
                    "5": "|| 2 ||  Retrouver mes aliments substitués."
                        }

CATEGORY_SELECTION = {
                    "0": "",
                    "1": "Sélectionnez la catégorie.",
                    "2": "",
                    "3": "|| 0 ||  Retourner au menu principale."
                        }

PRODUCT_SELECTION = {
                    "0": "",
                    "1": "Sélectionner un aliment.",
                    "2": "",
                    "3": "|| 0 ||  Retourner au menu principale."
                        }

SUBSTITUTE_SAVE_SELECTION = {
                    "0": "",
                    "1": "Voulez-vous enregistrer cet aliment?",
                    "2": "",
                    "3": "|| 0 ||  Retour au memu principal.",
                    "4": "|| 1 ||  Enregistrer l'aliment de substitution."
                        }

SUBSTITUTE_MENU_SELECTION = {
                    "0": "",
                    "1": "",
                    "2": "|| 0 ||  Retour au memu principal.",
                    "3": "|| 1 ||  Quitter le programme."
                        }

NO_SUBSTITUTE_SELECTION = {
                    "0": "",
                    "1": "L'alliment sélectionné dispose déjà du meilleur score nutritionnel.",
                    "2": "",
                    "3": "|| 0 ||  Retour au memu principal.",
                    "4": "|| 1 ||  Quitter le programme."
                        }

REGISTERED_SELECTION = {
                    "0": "",
                    "1": "Le produit à bien été enregistré.",
                    "2": "",
                    "3": "|| 0 ||  Retour au memu principal.",
                    "4": "|| 1 ||  Quitter le programme."
                        }
