# Projet 5 Openclassrooms - Utiliser les données publiques de l'OpenFoodFacts
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

--------------------
## Présentation du projet

Créer un programme qui récupère des aliments dans la base de données d'OpenFoodFacts, 
les comparer afin de proposer à l'utilisateur un substitut plus sain à l'aliment qu'il choisit.

## Description du parcours utilisateur

L'utilisateur ouvre le programme, ce dernier lui affiche les choix suivants:
```
1. Quel aliment souhaitez-vous remplacer?
2. Retrouver mes aliments substitués.
```
L'utilisateur sélectionne 1.   

Le programme pose les questions suivantes à l'utilisateur et ce dernier sélectionne les réponses :
* Sélectionnez la catégorie. 
>Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée.

* Sélectionnez l'aliment. 
>Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée.

L'utilisateur sélectionne l'aliment.
>Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.

* L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.
--------------------

## Installation de Mysql

>Vous pouvez consulter le cours sur l'installation et la connection de mysql [ici.](https://openclassrooms.com/fr/courses/1959476-administrez-vos-bases-de-donnees-avec-mysql/1959969-installez-mysql)

### Configuration et connexion à Mysql :
>Sous Windows
Téléchargez MySQL avec l'installeur (MSI Installer)[ici.](https://dev.mysql.com/downloads/mysql/#downloads), puis exécutez le fichier téléchargé. L'installeur démarre et vous guide lors de l'installation.

Exécutez la commande suivante dans l'invite de commande :
>**! Attention** aux guillemets autour des parties de chemin qui comportent un espace !
```
set PATH=%PATH%;chemin_vers_mysql_bin
Exemple :
set PATH=%PATH%;C:\"Program Files"\MySQL\"MySQL Server 8.0"\bin
```

Exécutez la commande suivante et entrez votre mot de passe:
```
mysql -h localhost -u root -p
```
>Sous Unix : Debian ou Ubuntu
Exécutez la commande suivante pour installer MySQL :
```
sudo apt-get install mysql-server mysql-client
```
>Une fois votre mot de passe introduit, MySQL va être installé.
Exécutez la commande suivante et entrer votre mot de passe:
```
mysql -h localhost -u root -p
``` 
### Création de la base de données Alimentation

**! Attention** aux sens des "/".  
```
mysql> SOURCE C:/Chemin_Vers_Mon_Dossier/create_database.sql
```

### Vider & Recréer les tables de la base de données Alimentation
```
mysql> SOURCE C:/Chemin_Vers_Mon_Dossier/initialize_alimentation.sql
```
--------------------

## Lancer le programme

Executez dans le terminal les commandes ci-dessous

>Installer le requirements.txt
```
Chemin/Vers_Mon_Dossier>pip3 install -r requirements.txt
```
>Remplir la base de données
```
Chemin/Vers_Mon_Dossier>python add_data_into_database.py
```
Attendez quelques secondes, jusqu'à avoir comme message :
```
Produits ajoutés à la base de données
```
>Lancer l'application
```
Chemin/Vers_Mon_Dossier>python main.py
```
--------------------

## Développé avec :
* [Python 3.9.2](https://www.python.org/downloads/release/python-392/)
* [Requests 2.25.1](https://pypi.org/project/requests/) 
* [mysql-connector-python 8.0.23](https://pypi.org/project/mysql-connector-python/)
* [Visual Studio Code](https://code.visualstudio.com/download)
