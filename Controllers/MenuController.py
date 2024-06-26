# MenuController
from Controllers.PlayerController import Admin
from Views.MainMenuView import MainMenuView
from Controllers.TournamentController import TournamentController
from Controllers.RapportController import RapportController


class MainController:
    def __init__(self):
        self.player_controller = Admin()
        self.tournament_controller = TournamentController()
        self.rapport_controller = RapportController()

    def start_menu(self):
        while True:
            choice = MainMenuView.main_menu()
            if choice == 1:
                self.start_menu_player()
            elif choice == 2:
                self.start_menu_tournament()
            elif choice == 3:
                self.rapport_manager()
            elif choice == 4:
                break  # quitter l'application
            else:
                print("Entrer un nombre entre 1 à 4")

    def start_menu_player(self):
        choice = MainMenuView.administration()
        while True:
            if choice == 1:
                self.player_controller.create_player()
                self.start_menu()
            elif choice == 2:
                self.player_controller.player_update()
                self.start_menu()
            elif choice == 3:
                self.player_controller.display_players()
                self.start_menu()
            elif choice == 4:
                self.start_menu()
            elif choice == 5:
                exit()
            else:
                print("Entrer un nombre entre 1 à 5")

    def start_menu_tournament(self):
        choice = MainMenuView.tournament_menu()
        while True:
            if choice == 1:
                self.tournament_controller.create_tournament()
                self.start_menu_tournament()
            elif choice == 2:
                self.tournament_controller.load_tournament()
                self.start_menu_tournament()
            elif choice == 3:
                self.start_menu()
            elif choice == 4:
                exit()
            else:
                print("Entrer un nombre entre 1 à 4")

    def rapport_manager(self):
        choice = MainMenuView.rapport_menu()
        while True:
            if choice == 1:
                self.rapport_controller.display_player()
                self.rapport_manager()
            elif choice == 2:
                self.rapport_controller.display_tournament()
                self.rapport_manager()
            elif choice == 3:
                self.rapport_controller.display_tournament_player()
                self.rapport_manager()
            elif choice == 4:
                self.rapport_controller.display_tournament_round_and_matches()
                self.rapport_manager()
            elif choice == 5:
                self.start_menu()
            elif choice == 6:
                exit()
            else:
                print("Entrer un nombre entre 1 à 6")
