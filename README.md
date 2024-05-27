<<<<<<< HEAD
# DA-Python-Code-P4-OC
Code P4 - Application Jeux d'échecs
=======

# Gestion de Tournois d'Échecs

## Vue d'ensemble

Ce programme est une application autonome et hors ligne pour la gestion des tournois d'échecs. Il est écrit en Python et utilise des fichiers JSON pour la persistance des données. Le programme permet de gérer les joueurs, les tournois, les tours et les matchs, ainsi que de générer des rapports sur les tournois et les joueurs.

## Prérequis

Avant de pouvoir exécuter le programme, assurez-vous d'avoir installé Python 3.x sur votre système. Vous aurez également besoin des bibliothèques Python listées dans le fichier `requirements.txt`.

## Installation

1. Clonez le repository contenant le code source du programme.
2. Naviguez dans le répertoire du projet.
3. Installez les dépendances en utilisant pip :

   ```sh
   pip install -r requirements.txt


## Structure du Projet
Le projet suit le modèle de conception MVC (Modèle-Vue-Contrôleur) et est organisé comme suit :

- `modeles/` : Contient les classes représentant les données (joueurs, tournois, tours, matchs).
- `vues/` : Contient les interfaces utilisateur (menus, rapports).
- `controleurs/` : Contient la logique de contrôle pour gérer les interactions entre les modèles et les vues.
- `data/` : Contient les fichiers JSON pour la persistance des données.
- `flake-report/` : Contient le rapport de flake8 pour la conformité au PEP 8.
- `README.md` : Ce fichier.
- `requirements.txt` : Liste des dépendances Python


## Utilisation

## Prérequis

Avant de commencer à utiliser ce projet, vous devez avoir installé Python sur votre système. Ce projet a été testé avec Python 3.x.

## Configuration de l'environnement

Il est recommandé d'utiliser un environnement virtuel pour exécuter ce projet afin de gérer les dépendances de manière isolée. Pour configurer et activer un environnement virtuel, suivez ces étapes :

### Création de l'environnement virtuel
Ouvrez un terminal (console) et exécutez la commande suivante à la racine de votre projet :
```bash
python3 -m venv 'nom_de_votre_environnement'      
```
### Pour activer l'environnement virtuel :   
Windows : 
```nom_de_votre_environnement\Scripts\activate```

MacOS et Linux : 
```source nom_de_votre_environnement/bin/activate```

Une fois l'environnement virtuel activé, votre invite de commande se positionnera dans le nouvel environnement virtuel.

### Installation des dépendances
Installez les dépendances nécessaires en exécutant :
```bash/python
pip install -r requirements.txt
```

### Exécution du code

Pour exécuter le programme, ouvrez une console et lancez la commande suivante depuis le répertoire du projet :

```sh
python main.py
```

Une fois le programme lancé, vous verrez un menu principal vous permettant d'effectuer les actions suivantes :

- Ajouter un joueur
- Lister tous les joueurs
- Créer un tournoi
- Lister tous les tournois
- Afficher les détails d'un tournoi
- Démarrer un nouveau tour
- Afficher les résultats des tours et des matchs

### Ajout d'un Joueur
Pour ajouter un joueur, sélectionnez l'option correspondante dans le menu principal et entrez les informations demandées (nom de famille, prénom, date de naissance, identifiant national d'échecs).

### Création d'un Tournoi
Pour créer un tournoi, sélectionnez l'option correspondante dans le menu principal et entrez les informations demandées (nom, lieu, dates de début et de fin, nombre de tours).

### Démarrage d'un Tour
Pour démarrer un nouveau tour, sélectionnez l'option correspondante dans le menu principal. Les paires de joueurs seront générées automatiquement en fonction des résultats des tours précédents.

### Affichage des Rapports
Vous pouvez afficher divers rapports sur les joueurs et les tournois en sélectionnant les options correspondantes dans le menu principal.


## Sauvegarde et Chargement des Données
Le programme sauvegarde automatiquement les données dans des fichiers JSON après chaque modification. Les fichiers JSON sont situés dans le répertoire data/. Lors du démarrage, le programme charge les données à partir de ces fichiers pour restaurer son état précédent.

## Conformité au PEP 8
Le code source est formaté selon les directives PEP 8. Utilisez flake8 pour vérifier la conformité :

```sh
flake8 --max-line-length=119 --format=html --htmldir=flake8_rapport
```
Le répertoire flake8_rapport contiendra un rapport HTML détaillant les éventuelles violations des directives PEP 8.

## Contribution
Pour contribuer au projet, veuillez 'forker' le dépôt, créer une branche de fonctionnalités, puis soumettre une pull request pour examen.


## Auteurs
Ce programme a été développé par Salim RIFFI.

## Licence
Ce projet est sous licence RIFFI Ltd.

## Contact
Pour toute question ou suggestion, n'hésitez pas à ouvrir un problème ("Issue") dans le dépôt GitHub du projet.


>>>>>>> 6f1b2a1 (ajout des fichiers README gitignore et requirements)
