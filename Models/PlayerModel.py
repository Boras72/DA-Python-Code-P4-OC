# PlayerModel
from tinydb import TinyDB, Query
from tinydb import where


class PlayerModel:
    db = TinyDB("data/players.json")
    player_table = db.table("_default")

    def __init__(self, name, firstname, birthdate, id, ranking, gender, points=0):
        # les attributs entre parenthèses sont initialisés par l'user
        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate
        self.id = id
        self.ranking = ranking
        self.gender = gender
        self.points = points  # Points dans le tournoi
        self.play_with = []  # liste des joueurs qui se sont déjà affrontés

    def gets_player_json(self):
        player_json = {
            "name": self.name,
            "firstname": self.firstname,
            "birthdate": self.birthdate,
            "id": self.id,
            "ranking": self.ranking,
            "gender": self.gender,
            "points": self.points,
        }
        return player_json

    def save(self):
        self.player_table.insert(self.gets_player_json())

    def update(self):
        Player = Query()
        player = self.gets_player_json()
        self.player_table.update(player, Player.id == self.id)

    @classmethod
    def get_all_players(cls):
        players = cls.player_table.all()
        players = sorted(
            players, key=lambda x: (x["name"], x["firstname"])
        )  # Pour trier les joueurs par ordre alphabétique
        player_object = []
        for player in players:
            player_object.append(PlayerModel(**player))

        return player_object

    @classmethod
    def update_player(cls, player):
        Player = Query()
        cls.player_table.update(player, Player.id == player["id"])

    @classmethod
    def get_player_by_id(cls, id):
        player = cls.player_table.search(where("id") == id)
        if player:
            return PlayerModel(**player[0])
        else:
            return None

    @classmethod
    def get_player_by_id_list(cls, id_list):
        players = []
        for id in id_list:
            player = cls.get_player_by_id(id)
            players.append(player)
        return players
