#TournamentView

class TournamentView():
	def __init__(self):  
		pass
	def create_tournament(self):
		name = input('Indiquez le nom du tournoi: ')
		start_date = input('Indiquez la date de début du tournoi: ')
		end_date = input('Indiquez la date de fin du tournoi: ')
		location = input('Indiquer le lieu du tournoi: ')
		description = input('Veuillez saisir un commentaire: ')
		#return {'name': name, 'start_date': start_date, 'end_date': end_date, 'location': location}
		return name, location, start_date, end_date, description


	def display_tournament(self, tournaments):          
		for tournament in tournaments :
			print(tournament.id, tournament.name, tournament.location)

	def get_tournament_id(self):
		choice = input("Entrer l'identifiant du tournoi")
		return choice

	def get_players_id(self):
		players_id = []
		while len(players_id) < 4:
			id = input("Entrer l'id du joueur: ")
			if id not in players_id:
				players_id.append(id)
			else:
				print("Ce joueur a déjà été ajouté")
		return players_id
					

