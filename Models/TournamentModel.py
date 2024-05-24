# Tournament : name, location, start_date, end_date, liste de joueurs, liste de rondes, nb de rondes, description.
from tinydb import TinyDB, Query
from tinydb import where
from .PlayerModel import PlayerModel


class TournamentModel:
    db = TinyDB("data/tournaments.json")
    tournament_table = db.table("tournament")

    def __init__(self, name, location, start_date, end_date, description, id=-1, players=[], rounds=[]):
        self.id = id
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.rounds = rounds
        self.round_number = 4
        self.round_actuel = 0
        self.description = description

    def gets_tournament_json(self):
        tournament_json = {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "players": self.players,
            "rounds": self.rounds,
            "id": self.id,
        }
        return tournament_json

    def save(self):
        tournament = self.gets_tournament_json()
        tournament_id = TournamentModel.gets_tournament_last_id()
        tournament.update({"id": tournament_id})
        self.tournament_table.insert(tournament)

    def update(self):
        Tournament = Query()
        tournament = self.gets_tournament_json()
        self.tournament_table.update(tournament, Tournament.id == self.id)

    def get_players(self):
        players = []
        for player_id in self.players:
            player = PlayerModel.get_player_by_id(player_id)
            players.append(player)
        return players

    def last_round_endded(self):  # indique q le round est terminé qd la 'end time' est indiquée (càd q tous les scores doivent être saisis)
        last_round = self.rounds[-1]
        if last_round["end_time"]:
            return True
        else:
            return False

    def add_round(self, round):
        self.rounds.append(round.get_round_json())  # liste des rounds contenant tous les rounds

    def get_matches(self):
        matches = []
        for round in self.rounds:
            matches.extend(round["matches"])
        return matches

    @classmethod
    def gets_tournament_last_id(cls):
        tournaments = cls.tournament_table.all()
        if tournaments:
            return int(tournaments[-1]["id"]) + 1
        else:
            return 1

    @classmethod
    def get_all_tournament(cls):
        tournaments = cls.tournament_table.all()
        tournament_object_list = []

        for tournament in tournaments:
            tournament_object = cls.tournament_json_to_object(tournament)
            tournament_object_list.append(tournament_object)

        return tournament_object_list

    @classmethod
    def tournament_json_to_object(cls, tournament):
        tournament_object = TournamentModel(**tournament)
        return tournament_object

    @classmethod
    def get_tournament_by_id(cls, id):
        tournament = cls.tournament_table.search(where("id") == int(id))
        if tournament:
            return cls.tournament_json_to_object(tournament[0])
        else:
            return None


# L'attribut round_number de la classe Tournament représente
# le numéro du tour actuel du tournoi.
# Il est initialisé à 0 lorsqu'un nouveau tournoi est créé. Au fur et à mesure
# que les tours sont joués,
# l'attribut round_number est incrémenté pour garder une trace du tour en cours.
# Cet attribut est utilisé pour déterminer quel tour de matchs jouer ensuite
# et pour générer des appariements pour les tours à venir.
