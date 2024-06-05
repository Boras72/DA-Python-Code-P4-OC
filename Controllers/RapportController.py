# Rapport Controller
from Models.PlayerModel import PlayerModel
from Models.TournamentModel import TournamentModel
from Models.RoundModel import RoundModel
from Views.PlayerView import PlayerView
from Views.TournamentView import TournamentView


class RapportController:
    def __init__(self):
        self.player_view = PlayerView()
        self.tournament_view = TournamentView()

    def display_player(self):
        # Liste de tous les joueurs par ordre alphabétique
        players = PlayerModel.get_all_players()
        self.player_view.display_player_view(players)

    def display_tournament(self):
        # Liste de tous les tournois
        tournaments = TournamentModel.get_all_tournament()
        self.tournament_view.display_tournament(tournaments)

    def display_tournament_player(self):
        # Liste des joueurs d'un tournoi par ordre alphabétique
        self.display_tournament()
        tournament_id = self.tournament_view.get_tournament_id()
        tournament = TournamentModel.get_tournament_by_id(tournament_id)
        players = PlayerModel.get_player_by_id_list(tournament.players)
        self.player_view.display_player_view(players)

    def display_tournament_round_and_matches(self):
        # Liste de tous les rounds et matches par tournoi
        self.display_tournament()
        tournament_id = self.tournament_view.get_tournament_id()
        rounds = RoundModel.get_round_by_tournament_id(tournament_id)  # liste des rounds par tournoi
        self.tournament_view.display_rounds(rounds)
