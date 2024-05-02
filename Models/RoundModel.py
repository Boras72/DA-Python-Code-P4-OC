# Round : contenant plusieurs matchs.

class RoundModel:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.end_time = None
        self.matchs = []
       
    def add_match(self, player1, player2):
        self.matchs.append(player1, player2)  
            #self.matchs.append(((player1, 0), (player2, 0)))
