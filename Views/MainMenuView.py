# MainMenuView


class MainMenuView:
    def ___init__(self):
        pass

    @staticmethod
    def rapport_menu():
        print("Que souhaitez vous faire ?")
        print("1.Afficher la liste de tous les joueurs par ordre alphabétique")
        print("2.Afficher la liste de tous les tournois")
        print("3.Afficher les joueurs d'un tournoi donné")
        print("4.Affichage de la liste de tous les tours du tournoi et de tous les matches du tour")
        print("5.Quitter le programme")

        choice = None
        while choice not in ["1", "2", "3", "4", "5"]:
            choice = input("Entrez votre choix: ")
        return int(choice)

    @staticmethod
    def main_menu():
        print("Que souhaitez vous faire ?")
        print("1.Administrer le club et ses membres")
        print("2.Créer et gérer un Tournoi")
        print("3.Gérer des rapports")
        print("4.Quitter le programme")

        choice = None
        while choice not in ["1", "2", "3", "4"]:
            choice = input("Entrez votre choix: ")
        return int(choice)

    @staticmethod  # pour appeler la méthode avec sa classe
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
    def tournament_menu():
        print("Que souhaitez vous faire ?")  # Menu pour la gestion des tournois
        print("1.Créer un Tournoi")
        print("2.Gérer un Tournoi")
        print("3.Retour au menu principal")
        print("4.Quitter le programme")

        choice = None
        while choice not in ["1", "2", "3", "4"]:
            choice = input("Entrez votre choix: ")
        return int(choice)
