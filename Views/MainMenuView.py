#MainMenuView

from Views.PlayerView import PlayerView
from Views.TournamentView import TournamentView
from Controllers.PlayerController import Admin

class MainMenuView:
    def ___init__(self): 
        pass
    @staticmethod
    def main_menu():
        print("Que souhaitez vous faire ?")
        print("1.Administrer le club et ses membres")
        print("2.Créer et gérer un Tournoi")
        print("3.Gérer des rapports")
        print("4.Quitter le programme")

        choice=None
        while choice not in ["1","2","3","4"]:
            choice=input("Entrez votre choix :")
        return int(choice)
        
    @staticmethod                               #pour appeler la méthode avec sa classe 
    def administration():                       #Menu pour la gestion de joueurs
        print("Que souhaitez vous faire ?")                    
        print("1.Ajouter un joueur")
        print("2.Modifier les informations d'un joueur")
        print("3.Afficher la liste des joueurs")
        print("4.Retour au menu principal")
        print("5.Quitter le programme")

        choice=None
        while choice not in ["1","2","3","4","5"]:
            choice=input("Entrez votre choix :")
        return int(choice)

    @staticmethod
    def tournament_menu():
        print("Que souhaitez vous faire ?")             #Menu pour la gestion des tournois
        print("1.Créer un Tournoi")
        print("2.Gérer un Tournoi")
        print("3.Retour au menu principal")
        print("4.Quitter le programme")
        
        choice=None
        while choice not in ["1","2","3","4"]:
            choice=input("Entrez votre choix :")
        return int(choice)
    
    


    """
        match choice :
                case "1":
                    create_player()
                case "2":


                    tournament_view=TournamentView()  #var créée pour créer une instance de la classe tournamentView
                    tournament=tournament_view.create_tournament() # Exécuter la méthode create.tournament en utilisant la var "tournament" car présence d'un return dans la méthode "create_tournament"
                    tournament_view.display_tournament("Euro_game_chess","Hambourg")  #Exécution de la méthode "display_tournament" 
                    print(tournament)
        return int(input('Quel est votre choix ?'))
    """

    
    