# PlayerView
from rich.console import Console
from rich.table import Table
import re


class PlayerView:
    def create_player(self):
        name = input("Quel est votre nom ? ")
        firstname = input("Quel est votre prénom ? ")
        id = input("Quel est votre id ? ")
        birthdate = input("Quel est votre date de naissance (JJ/MM/AAAA) ? ")
        regex_date = r"\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b"
        while not re.match(regex_date, birthdate):
            print("Format de la date incorrecte")
            birthdate = input("Quel est votre date de naissance (JJ/MM/AAAA) ? ")
        gender = input("Quel est votre genre ? ")
        ranking = input("Quel est votre classement ? ")
        return name, firstname, birthdate, id, ranking, gender

    def display_player(self, name, age):
        print(name, age)

    def modify_player_id(self):
        print("Veuillez entrer l'id du joueur à modifier: ")
        id = input("numéro de l'id ")
        return id

    def modify_player_new_value(self):
        print("Entrer votre modification")

    def player_update_view(self, player):
        print("Tapez ENTREE pour conserver l'ancienne valeur")
        name = input(f"Nom ({player.name}): ") or player.name
        firstname = input(f"Prénom ({player.firstname}): ") or player.firstname
        birthdate = input(f"Date de Naissance ({player.birthdate}): ") or player.birthdate
        ranking = input(f"Classement ({player.ranking}): ") or player.ranking
        gender = input(f"Genre ({player.gender}): ") or player.gender
        return name, firstname, birthdate, ranking, gender

    def display_player_view(self, players):

        table = Table(title="Liste des joueurs")

        table.add_column("Id", style="white", no_wrap=True)
        table.add_column("Name", style="magenta")
        table.add_column("Firstname", justify="right", style="cyan")
        table.add_column("Birthdate", justify="right", style="blue")
        table.add_column("Ranking", justify="right", style="red")
        table.add_column("Gender", justify="right", style="green")

        for player in players:
            table.add_row(player.id, player.name, player.firstname, player.birthdate, player.ranking, player.gender)

        console = Console()
        console.print(table)
