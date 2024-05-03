# main.py (fichier principal pour initialisez et lancez l'application)

from Controllers.MenuController import MainController
#importer la classe [from nom_dossier.nom_fichier import nom_class]

if __name__ == '__main__':
    MainController().start_menu()   
    #On appelle la fonction start_menu de la classe MainController qui elle-même va exécuter la fonction mainmenu dans la classe Mainmenuview
