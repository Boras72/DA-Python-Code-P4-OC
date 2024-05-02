#PlayerView
from Controllers.db import load_db

class PlayerView:
	def create_player(self):
		name = input('Quel est votre nom ?')
		firstname = input('Quel est votre prénom ?')
		id = input('Quel est votre id ?')
		birthdate = input('Quel est votre date de naissance ?')
		gender = input('Quel est votre genre ?')
		ranking = input('Quel est votre classement ?')
		return {'name': name, 'firstname' : firstname, 'birthdate': birthdate, 'id': id, 'ranking': ranking,'gender': gender, }

	def display_player(self, name, age):  
		print(name, age)

	def modify_player_id(self):
		print("Veuillez entrer l'id du joueur à modifier: ")
		id=input("numéro de l'id ")
		return id

	def modify_player_information(self, id):
		#print(id)
		db_players=load_db("players")
		player_found=None
		for player in db_players:
			print(db_players)
			print(player)
			if player["id"]==2:
				print("ok")
				"""print(player["id"])
				player_found=player
				print("Utilisateur trouvé")
				
			else:
				print("Utilisateur non trouvé")
				return                                                     # le return ici sert pour sortir de la Fn si joueur non trouvé
		player = player_found"""
		
		print("Que souhaitez vous modifier ?")
		print(f"1.nom: {player['name']}")
		print(f"2.prénom: {player['firstname']}")
		print(f"3.date de naissance: {player['birthdate']}")
		print(f"4.classement: {player['ranking']}")
		print(f"5.genre: {player['gender']}")
		choice=None
		while choice not in ["1","2","3","4","5"]:
			choice = input("Votre choix")
		return choice

	def modify_player_new_value(self):
		print("Entrer votre modification")
		new_info=input("Entre la nouvelle information")

	def player_update_view(self,player):
		print("Tapez ENTREE pour conserver l'ancienne valeur")
		name = input(f"Nom ({player.name}): ") or player.name
		firstname = input(f"Prénom ({player.firstname}): ") or player.firstname
		birthdate = input(f"Date de Naissance ({player.birthdate}): ") or player.birthdate
		ranking = input(f"Classement ({player.ranking}): ") or player.ranking
		gender = input(f"Genre ({player.gender}): ") or player.gender
		return name,firstname,birthdate,ranking,gender

	def display_player_view(self, players):
		print("La liste des joueurs")
		for player in players:
			print(player.id, player.name, player.firstname, player.birthdate, player.ranking, player.gender)
			