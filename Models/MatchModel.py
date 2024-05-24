# Match : players, result.


class MatchModel:
    def __init__(self, id, player1, player2):
        self.id = id
        self.player1 = player1
        self.player2 = player2
        self.result = None

    def set_result(self, result):  # changer résultat
        self.result = result

    def get_result(self):  # retourner le résultat
        return self.result


# action=méthode / info=attribut
# lier des actions=models
