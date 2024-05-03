from Models.TournamentModel import TournamentModel
from Views.TournamentView import TournamentView

class TournamentController():
    
    def create_tournament(self):
        tournament_view=TournamentView()
        #user_input=tournament_view.create_tournament()
        #tournament=TournamentModel(user_input["name"],user_input["start_date"],user_input["end_date"],user_input["location"], user_input["description"]) 
        #return tournament
        name, location, start_date, end_date, description = tournament_view.create_tournament()
        tournament = TournamentModel(name, location, start_date, end_date, description)
        tournament.save()

    def play_tournament(self, tournament, new_tournament):
        while True:
            nb_round = tournament.round_number        #"tournament"= instance (on nomme l'instance comme on veut)
            for i in range(nb_round):
                pass
                
    def load_tournament(self):
        pass