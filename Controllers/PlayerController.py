from Models.PlayerModel import PlayerModel
from Views.PlayerView import PlayerView
from Controllers.db import save_db, load_db, update_db
from Views.TournamentView import TournamentView
from Models.TournamentModel import TournamentModel


class Admin:            
    def __init__(self):
        pass
    
    def create_player(self):
        player_view=PlayerView()      #definir une instance de la classe player_view
        #user_input=player_view.create_player()
        name, firstname, birthdate, id, ranking, gender = player_view.create_player()
        #Récupération des infos du joueur
        #player=PlayerModel(user_input["name"],user_input["firstname"],user_input["birthdate"],user_input["id"],user_input["ranking"],user_input["gender"])#var player = instance de la classe player model
        player = PlayerModel(name, firstname, birthdate, id, ranking, gender)
        player.save()
        #player_json=player.gets_player_json()
        #save_db("players",player_json)
        #return player

    """
    @staticmethod
    def modify_player(player_id, choice):
        db_players=load_db("players")
        player_found=None
        for player in db_players:
            if player["id"]==player_id:
                player_found=player
                break
        if player_found is None:
            print("utilisateur non trouvé")
            return   # le return ici sert pour sortir de la Fn si joueur non trouvé
        
        #print("Si vous voulez entrer votre modification, saisissez votre modification, sinon cliquez sur Entrée")
        if choice == 1 :
            new_name=input("Entrez le nouveau nom de l'utilisateur") or player_found["name"]
            print("new_name",new_name)
        elif choice == 2 :
            new_first_name=input("Entrez le nouveau prénom de l'utilisateur") or player_found["firstname"]
        elif choice == 3 :
            new_birthdate=input("Entrez le nouveau birthdate de l'utilisateur") or player_found["birthdate"]
        elif choice == 4 :
            new_ranking=input("Entrez le nouveau ranking de l'utilisateur") or player_found["ranking"]
        elif choice == 5 :
            new_gender=input("Entrez le nouveau gender de l'utilisateur") or player_found["gender"]

        update_player=PlayerModel(new_name, new_first_name, new_birthdate, new_id, new_ranking, new_gender)

        update_player_json=update_player.gets_player_json()
        update_db("players",update_player_json)
        return update_player"""

    def player_update (self):
        playerview=PlayerView() 
        id=playerview.modify_player_id()          
        #choice=playerview.modify_player_information(id) 
        #Admin.modify_player(id, choice)  
        player=PlayerModel.get_player_by_id(id)  
        name, firstname, birthdate, ranking, gender = playerview.player_update_view(player)  
        player.name=name 
        player.firstname=firstname
        player.birthdate=birthdate  
        player.ranking=ranking
        player.gender=gender
        PlayerModel.update_player(player.gets_player_json())



    def display_players(self):
        """db_players=load_db("players")
        i=1
        for player in db_players:
            print(f"Nom du Player {i}:", player ["name"])
            i=i+1"""
        players = PlayerModel.get_all_players()
        playerview=PlayerView()
        playerview.display_player_view(players)

        


