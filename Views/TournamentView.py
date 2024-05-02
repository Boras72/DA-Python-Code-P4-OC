#TournamentView

class TournamentView():
	def __init__(self):  #Nouveau
		pass
	def create_tournament(self):
		name = input('Indiquez le nom du tournoi ?')
		start_date = input('Indiquez la date de début du tournoi ?')
		end_date = input('Indiquez la date de fin du tournoi ?')
		location = input('Quel est le lieu du tournoi ?')
		return {'name': name, 'start_date': start_date, 'end_date': end_date, 'location': location}

	def display_tournament(self, name, location):          #Pourquoi ?
		print(name, location)