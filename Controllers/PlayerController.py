# PlayerController
from Models.PlayerModel import PlayerModel
from Views.PlayerView import PlayerView


class Admin:
    def __init__(self):
        pass

    def create_player(self):
        # definir une instance de la vue
        player_view = PlayerView()
        # récupération des infos du joueur à la vue
        name, firstname, birthdate, id, ranking, gender = player_view.create_player()
        # Renvoyez/Passez les infos du joueur au Model
        player = PlayerModel(name, firstname, birthdate, id, ranking, gender)
        # Sauvegarder le joueur grâce au Model
        player.save()

    def player_update(self):
        playerview = PlayerView()
        self.display_players()
        id = playerview.modify_player_id()
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
