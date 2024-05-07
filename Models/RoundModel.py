# Round : contenant plusieurs matchs.
from tinydb import TinyDB, Query
from tinydb import where

class RoundModel:
    db=TinyDB("data/tournaments.json")
    round_table=db.table("round")
    def __init__(self, name, tournament_id, id=-1, start_time = None, end_time = None, matchs = []):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.matchs = matchs
        self.id = id
        self.tournament_id = tournament_id
       
    def add_match(self, player1, player2):
        self.matchs.append(player1, player2)  
            #self.matchs.append(((player1, 0), (player2, 0)))

    def get_round_json(self):
        round_json={"name": self.name, "tournament_id": self.tournament_id, "id": self.id, "start_time": self.start_time, "end_time": self.end_time, "matchs": self.matchs}
        return round_json


    def save(self):
        round = self.get_round_json()
        round_id = RoundModel.get_round_last_id()
        round.update({"id":round_id})
        self.round_table.insert(round) 

    @classmethod
    def get_round_last_id(cls):
        rounds = cls.round_table.all()
        if rounds:
            return int(rounds[-1]["id"])+1
        else: 
            return 1

