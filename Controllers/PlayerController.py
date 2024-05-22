from Models.PlayerModel import PlayerModel
from Views.PlayerView import PlayerView


class Admin:
    def __init__(self):
        pass

    def create_player(self):
        player_view = PlayerView()  # definir une instance de la classe player_view
        # user_input=player_view.create_player()
        name, firstname, birthdate, id, ranking, gender = player_view.create_player()
        # Récupération des infos du joueur
        player = PlayerModel(name, firstname, birthdate, id, ranking, gender)
        player.save()
        # player_json=player.gets_player_json()
        # save_db("players",player_json)
        # return player

    def player_update(self):
        playerview = PlayerView()
        id = playerview.modify_player_id()
        # choice=playerview.modify_player_information(id)
        # Admin.modify_player(id, choice)
        player = PlayerModel.get_player_by_id(id)
        name, firstname, birthdate, ranking, gender = playerview.player_update_view(player)
        player.name = name
        player.firstname = firstname
        player.birthdate = birthdate
        player.ranking = ranking
        player.gender = gender
        PlayerModel.update_player(player.gets_player_json())

    def display_players(self):
        players = PlayerModel.get_all_players()
        playerview = PlayerView()
        playerview.display_player_view(players)
