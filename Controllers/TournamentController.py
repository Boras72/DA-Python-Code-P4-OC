from Models.TournamentModel import TournamentModel
from Views.TournamentView import TournamentView
from .PlayerController import Admin

class TournamentController():
    def __init__(self):
        self.tournament_view=TournamentView()
    def create_tournament(self):
        #user_input=tournament_view.create_tournament()
        #tournament=TournamentModel(user_input["name"],user_input["start_date"],user_input["end_date"],user_input["location"], user_input["description"]) 
        #return tournament
        name, location, start_date, end_date, description = self.tournament_view.create_tournament()
        tournament = TournamentModel(name, location, start_date, end_date, description)
        tournament.save()

    def play_tournament(self, tournament, new_tournament):
        while True:
            nb_round = tournament.round_number        #"tournament"= instance (on nomme l'instance comme on veut)
            for i in range(nb_round):
                pass
                
    def load_tournament(self):
        tournaments = TournamentModel.get_all_tournament()
        self.tournament_view.display_tournament(tournaments)
        tournament_id = self.tournament_view.get_tournament_id()
        tournament = TournamentModel.get_tournament_by_id(tournament_id)
        state_number, tour_number = self.tournament_state(tournament)
        
        if state_number == 1:
            self.add_tournament_players()


    def tournament_state(self, tournament):
        # vérifier si les joueurs sont ajoutés
        # vérifier si les tours ont commencé
        # vérifier si les scores des tours ont été ajoutés
        #
        # retourner l'état du tournoi : (2 paramètres)
        # 1. Ajouter les joueurs (N°state + None)
        # 2. Démarrer un tour (N°state + N° tour à démarrer)
        # 3. Ajouter les scores d'un tour (N°state + N° tour concerné par les scores)
        
        if tournament.players:
            return 2, None
        else:
            return 1, None
        

    def add_tournament_players(self):
        Admin().display_players()

