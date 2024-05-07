# Player : name, firstname, birthdate, id, ranking, gender
from tinydb import TinyDB, Query
from tinydb import where

class PlayerModel:
    db=TinyDB("data/players.json")
    player_table=db.table("_default")
    def __init__(self, name, firstname, birthdate, id, ranking, gender, score=0):
#les attributs entre parenthèses sont initialisés par l'user
        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate
        self.id = id
        self.ranking = ranking
        self.gender = gender
        self.score = score   # Points dans le tournoi 
        self.play_with = [] #liste des joueurs déjà affrontés 


    def gets_player_json(self):
        player_json={"name": self.name, "firstname": self.firstname, "birthdate": self.birthdate, "id": self.id, "ranking": self.ranking, "gender": self.gender, "score": self.score}
        return player_json  

    def save(self):
        self.player_table.insert(self.gets_player_json())

    @classmethod
    def get_all_players(cls):
        players=cls.player_table.all()

        player_object=[]
        for player in players:
            player_object.append(PlayerModel(**player))

        return player_object

    
    @classmethod
    def update_player(cls, player):
        Player = Query()
        cls.player_table.update(player, Player.id==player["id"])
        


    @classmethod
    def get_player_by_id(cls,id):
        player=cls.player_table.search(where("id")==id)
        if player:
            return PlayerModel(**player[0]) 
        else:
            return None

