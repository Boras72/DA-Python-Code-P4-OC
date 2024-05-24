# MainMenuView


class MainMenuView:
    def __init__(self):
        pass            # Pkoi pass ?"

    @staticmethod    # @staticmethod ?   # pour appeler la méthode avec sa classe ???
    def main_menu():
        print("Que souhaitez vous faire ?")
        print("1.Administrer le club et ses membres")  #renvoie à la méthode 'administration'
        print("2.Créer et gérer un Tournoi")     #renvoie à la méthode 'tournament_menu'
        print("3.Gérer des rapports")      #renvoie à la méthode 'rapport_menu'
        print("4.Quitter le programme")

        choice = None                               # choice =  None ?
        while choice not in ["1", "2", "3", "4"]:   #TQ le input est different de 1,2,3,4
            choice = input("Entrez votre choix: ")
        return int(choice)                          # Alors retourner le input("") au format int

    @staticmethod  
    def administration():  # Menu pour la gestion de joueurs
        print("Que souhaitez vous faire ?")
        print("1.Ajouter un joueur")
        print("2.Modifier les informations d'un joueur")
        print("3.Afficher la liste des joueurs")
        print("4.Retour au menu principal")
        print("5.Quitter le programme")

        choice = None
        while choice not in ["1", "2", "3", "4", "5"]:
            choice = input("Entrez votre choix: ")
        return int(choice)

    @staticmethod
    def tournament_menu():                   # Menu pour la gestion des tournois
        print("Que souhaitez vous faire ?")  
        print("1.Créer un Tournoi")
        print("2.Gérer un Tournoi")
        print("3.Retour au menu principal")
        print("4.Quitter le programme")

        choice = None
        while choice not in ["1", "2", "3", "4"]:
            choice = input("Entrez votre choix: ")
        return int(choice)
    
    @staticmethod
    def rapport_menu():                          # Menu pour la gestion des rapports
        print("Que souhaitez vous faire ?")
        print("1.Afficher la liste de tous les joueurs par ordre alphabétique")
        print("2.Afficher la liste de tous les tournois")
        print("3.Afficher les joueurs d'un tournoi donné")
        print("4.Afficher la liste de tous les rounds et matches d'un tournoi")
        print("5.Retour au menu principal")
        print("6.Quitter le programme")

        choice = None
        while choice not in ["1", "2", "3", "4", "5", "6"]:
            choice = input("Entrez votre choix: ")
        return int(choice)
