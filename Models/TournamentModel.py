# Tournament : name, location, start_date, end_date, liste de joueurs, liste de rondes, nb de rondes, description.

class TournamentModel:
    def __init__(self, name, location, start_date, end_date, description):
        self.id = -1
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.players = []
        self.rounds = []
        self.round_number = 4
        self.round_actuel = 0
        self.description = description

    def gets_tournament_json(self):
        tournament_json={"name": self.name, "location": self.location, "start_date": self.start_date, "end_date": self.end_date, "description": self.description, "players":self.players, "rounds":self.rounds}
        return tournament_json

    def create_player_pairs(self, round_actuel):
        if round_actuel == 0:
            liste_players = sorted(self.players, key=lambda x:(x.score, random.random()))  # sorted= méthode de tri ici aléatoire  (liste trié aléatoire)
        else:
            liste_players_score = sorted(self.players, key=lambda x:x.score, reverse=True)  #tri dans un ordre décroissant (liste triée décroissant)
            i == 0
            pairs_players = []
            while i < len(liste_players_score)-1:                       #i=while
                player1 = liste_players_score[i]
                player2 = liste_players_score[i+1]
                if  player2 not in player1.play_with:
                    pairs_players.append((player1, player2))
                    player1.play_with.append(player2)
                    player2.play_with.append(player1)
                    i+=2
                else:
                    for j in range(i+2, len(liste_players_score)):                      #j=for
                        if liste_players_score[j] not in player1.play_with:
                            player2=liste_players_score[j]      #player2=new player2 =>j
                            liste_players_score[i+1],liste_players_score[j]=liste_players_score[j],liste_players_score[i+1]  #pour réarranger l'ordre des joueurs (le nv joueur 2 prend la place de l'ancien joueur2)
                            pairs_players.append((player1, player2))
                            player1.play_with.append(player2)
                            player2.play_with.append(player1)
                            i+=2                                            #next(i=i+2)
                            break
        return pairs_players       





                       







        
#L'attribut round_number de la classe Tournament représente le numéro du tour actuel du tournoi. 
#Il est initialisé à 0 lorsqu'un nouveau tournoi est créé. Au fur et à mesure que les tours sont joués, 
#l'attribut round_number est incrémenté pour garder une trace du tour en cours. 
#Cet attribut est utilisé pour déterminer quel tour de matchs jouer ensuite et pour générer des appariements pour les tours à venir.