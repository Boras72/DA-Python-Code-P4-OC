# main.py (fichier principal pour initialiser et lancer l'application) :

from Controllers.MenuController import MainController

# importer la classe => [from nom_dossier.nom_fichier import nom_class]

if __name__ == "__main__":
    MainController().start_menu()
    """
    Appel de la fonction start_menu de la classe MainController (import MainController)
    qui va exécuter elle-même la fonction Mainmenu dans la classe Mainmenuview
    """
