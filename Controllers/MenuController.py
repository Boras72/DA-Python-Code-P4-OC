from Controllers.PlayerController import Admin
from Models.PlayerModel import PlayerModel
from Views.PlayerView import PlayerView
from Models.TournamentModel import TournamentModel
from Views.TournamentView import TournamentView
from Controllers.db import save_db,load_db
from Views.MainMenuView import MainMenuView
from Controllers.TournamentController import TournamentController

class MainController():
	def __init__(self):
		self.player_controller=Admin()
		self.tournament_controller = TournamentController()
	def start_menu(self):
		while True :
			choice = MainMenuView.main_menu()
			if choice == 1:
				self.start_menu_player()	
			elif choice == 2:
				self.start_menu_tournament()
			elif choice == 3:
				print("gérer les rapports")
			elif choice == 4:
				break					#quitter l'application
			else:
				print("Entrer un nombre entre 1 à 4")
			

	def start_menu_player(self):
		choice = MainMenuView.administration()
		while True :
			if choice == 1:
				self.player_controller.create_player()
				self.start_menu()
			elif choice == 2:
				"""playerview=PlayerView()  # x(instance)=class(Playerview)
				id=playerview.modify_player_id()  #y(var)=instance.methode
				choice=playerview.modify_player_information(id) #w(var)
				Admin.modify_player(id, choice)   # appel du controller avec sa classe Admin"""
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
		while True :
			if choice == 1:
				self.tournament_controller.create_tournament()
			elif choice == 2:
				self.tournament_controller.load_tournament()
				self.start_menu()
			elif choice == 3:
				self.start_menu()
			elif choice == 4:
				exit()
			else:
				print("Entrer un nombre entre 1 à 4")




	

		
