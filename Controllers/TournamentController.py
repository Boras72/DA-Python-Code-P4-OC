from Models.TournamentModel import TournamentModel
from Views.TournamentView import TournamentView

class tournamentcontroller():
    @staticmethod
    def create_tournament():
        tournament_view=TournamentView()
        user_input=tournament_view.create_tournament()
        tournament=TournamentModel(user_input["name"],user_input["start_date"],user_input["end_date"],user_input["location"], user_input["description"]) 
        return tournament

    def play_tournament(self, tournament, new_tournament):
        while True:
            nb_round = tournament.round_number        #"tournament"= instance (on nomme l'instance comme on veut)
            for i in range(nb_round):
                
