from Models.TournamentModel import TournamentModel
from Views.TournamentView import TournamentView
from .PlayerController import Admin
from Models.RoundModel import RoundModel
from datetime import datetime

class TournamentController():
    def __init__(self):
        self.tournament_view=TournamentView()
    def create_tournament(self):
        #user_input=tournament_view.create_tournament()
        #tournament=TournamentModel(user_input["name"],user_input["start_date"],user_input["end_date"],user_input["location"], user_input["description"]) 
        #return tournament
        name, location, start_date, end_date, description = self.tournament_view.create_tournament()
        tournament = TournamentModel(name, location, start_date, end_date, description)
        tournament.save()

    def play_tournament(self, tournament, new_tournament):
        while True:
            nb_round = tournament.round_number        #"tournament"= instance (on nomme l'instance comme on veut)
            for i in range(nb_round):
                pass
                
    def load_tournament(self):
        tournaments = TournamentModel.get_all_tournament()
        self.tournament_view.display_tournament(tournaments)
        tournament_id = self.tournament_view.get_tournament_id()
        tournament = TournamentModel.get_tournament_by_id(tournament_id)
        state_number, round_number = self.tournament_state(tournament)
        
        if state_number == 1:                   # Un tournoi peut se trouver dans 3 états
            self.add_tournament_players(tournament)
        elif state_number == 2:
            self.start_round(round_number, tournament)

    def tournament_state(self, tournament):
        # vérifier si les joueurs sont ajoutés
        # vérifier si les tours ont commencé
        # vérifier si les scores des tours ont été ajoutés
        #
        # retourner l'état du tournoi : (2 paramètres)
        # 1. Ajouter les joueurs (N°state + None)
        # 2. Démarrer un tour (N°state + N° tour à démarrer)
        # 3. Ajouter les scores d'un tour (N°state + N° tour concerné par les scores)
        
        if tournament.players:
            if tournament.rounds:
                pass
            else:
                return 2, 1
        else:
            return 1, None
        

    def add_tournament_players(self, tournament):
        Admin().display_players()
        player_id = self.tournament_view.get_players_id()
        tournament.players = player_id
        tournament.update()

    def start_round(self, round_number, tournament):
        # 1.Récupérer les joueurs du tournoi
        players = tournament.get_players()
        # 2.Créer le tour (round)
        round = RoundModel(name=f"Round {round_number}", tournament_id = tournament.id, start_time=str(datetime.now()))
        round.save()   
        # 3.Générer les matches: 
        #   - Trier les joueurs
        #   - Associer les joueurs
        players = sorted(players, key=lambda player:player.score, reverse=True)  # tri des joueurs
        #associer les joueurs
        tournament_matches = tournament.get_matches()  #matches du tournoi
        round_matches = []    #rounds des matches actuels
        for player_1 in players:
            for player_2 in players:
                if player_1.id != player_2.id:
                    match = ([player_1.id, 0], [player_2.id, 0])
                    #- vérifier que l'un des joueurs n'as pas joué de matchs dans le round en cours
                    if not self.chek_if_match_in_round_matches(match, round_matches):
                        # - vérifier que les 2 joueurs ne se sont pas déjà affrontés dans le tournoi
                        if not self.chek_if_match_in_tournament_matches(match, tournament_matches):
                            round_matches.append(match)
        # 4.Ajouter les matches au round
        round.matches = round_matches
        round.update()    
        # 5.Ajouter le round au tournoi
        tournament.add_round(round)
        tournament.update()
        # 6.Mettre à jour les scores des matches du tour
        
    def chek_if_match_in_round_matches(self, match, round_matches): 
        for round_match in round_matches:
            p1 = match[0][0]  #=player1  [N°liste]  [indexe] NOUVEAUX JOUEURS A METTRE DANS UN MATCH
            p2 = match[1][0]  #=player 2  (current match)
            rp1 = round_match[0][0]   #(round match_player)  JOUEURS QUI ONT DEJA JOUES DES MATCHES
            rp2 = round_match[1][0]
            # si l'une de ces cond est vérifiée çàd q un joueur a déjà joué un de ces matches
            if p1 == rp1 or p1 == rp2 or p2 == rp1 or p2 == rp2: 
                return True
        return False

    def chek_if_match_in_tournament_matches(self, match, tournament_matches):   
        for tournament_match in tournament_matches:  #"tournament_matches"=tous les matches qui ont déjà eu lieu
            # vérifier que les 2 joueurs se sont déjà affrontés dans le tournoi
            p1 = match[0][0]  #=player1  [N°liste]  [indexe]
            p2 = match[1][0]  #=player 2  (current match)
            tp1 = tournament_match[0][0]   #(tournament match_player) MATCHES QUI NE SONT PAS DU ROUND ACTUEL + MATCHES DES ROUNDS PASSES
            tp2 = tournament_match[1][0]           
            if (p1 == tp1 and p2 == tp2) or (p1 == tp2 and p2 == tp1):
                return True
        return False









