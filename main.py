#main.py (fichier principal pour initialisez et lancez l'application) connecté au MainController qui est le moteur, le main d'oeuvre de ce programme alors que main.py n'est que le déclencheur

from Controllers.MenuController import MainController
#importer la classe [from nom_dossier.nom_fichier import nom_class]

if __name__ == '__main__':
    MainController().start_menu()   
    #On appelle la fonction start_menu de la classe MainController qui elle-même va exécuter la fonction mainmenu dans la classe Mainmenuview
