# Round : contenant plusieurs matchs.
from tinydb import TinyDB, Query
from tinydb import where

class RoundModel:
    db=TinyDB("data/tournaments.json")
    round_table=db.table("round")
    def __init__(self, name, tournament_id, id=-1, start_time = None, end_time = None, matches = []):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.matches = matches
        self.id = id
        self.tournament_id = tournament_id
       
    def add_match(self, match):
        self.matches.append(match)  
            

    def get_round_json(self):
        round_json={"name": self.name, "tournament_id": self.tournament_id, "id": self.id, "start_time": self.start_time, "end_time": self.end_time, "matches": self.matches}
        return round_json

    def update(self):
        Round = Query()
        round = self.get_round_json()
        print(round)
        self.round_table.update(round, Round.id == self.id)

    def save(self):
        round = self.get_round_json()
        round_id = RoundModel.get_round_last_id()
        round.update({"id":round_id})
        self.id = round_id
        self.round_table.insert(round) 

    @classmethod
    def get_round_last_id(cls):
        rounds = cls.round_table.all()
        if rounds:
            return int(rounds[-1]["id"])+1
        else: 
            return 1

    @classmethod
    def get_round_by_id(cls,id):
        round=cls.round_table.search(where("id")==int(id))
        if round:
            return cls.round_json_to_object(round[0])
        else:
            return None