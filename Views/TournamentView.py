# TournamentView
from rich.console import Console
from rich.table import Table


class TournamentView:
    def __init__(self):
        pass

    def create_tournament(self):
        name = input("Indiquez le nom du tournoi: ")
        start_date = input("Indiquez la date de début du tournoi: ")
        end_date = input("Indiquez la date de fin du tournoi: ")
        location = input("Indiquer le lieu du tournoi: ")
        description = input("Veuillez saisir un commentaire: ")
        # return {'name': name, 'start_date': start_date, 'end_date': end_date, 'location': location}
        return name, location, start_date, end_date, description

    def display_tournament(self, tournaments):
        table = Table(title="Liste des tournois")
        table.add_column("Id", style="cyan", no_wrap=True)
        table.add_column("Name", style="magenta")
        table.add_column("Location", justify="right", style="green")
        table.add_column("Start date", justify="right", style="green")
        table.add_column("End date", justify="right", style="green")
        table.add_column("Description", justify="right", style="green")

        for tournament in tournaments:
            table.add_row(
                str(tournament.id),
                tournament.name,
                tournament.location,
                tournament.start_date,
                tournament.end_date,
                tournament.description,
            )

        console = Console()
        console.print(table)

    def display_rounds(self, rounds):
        console = Console()
        for round in rounds:
            table = Table(title=f"{round.name}")
            table.add_column("Id", style="cyan", no_wrap=True)
            table.add_column("Name", style="cyan", no_wrap=True)
            table.add_column("Start time", style="cyan", no_wrap=True)
            table.add_column("End time", style="cyan", no_wrap=True)
            table.add_column("Status", style="cyan", no_wrap=True)

            status = "terminé" if round.end_time else "en cours"

            table.add_row(str(round.id), round.name, round.start_time, round.end_time, status)

            console.print(table)
            table = Table(title=f"Liste des matches du {round.name}")
            table.add_column("Player1", style="cyan", no_wrap=True)
            table.add_column("Score P1", style="cyan", no_wrap=True)
            table.add_column("Vs.", style="cyan", no_wrap=True)
            table.add_column("Score P2", style="cyan", no_wrap=True)
            table.add_column("Player2", style="cyan", no_wrap=True)

            for match in round.matches:
                table.add_row(match[0][0], str(match[0][1]), "Vs", str(match[1][1]), match[1][0])
            console.print(table)

    def get_tournament_id(self):
        choice = input("Entrer l'identifiant du tournoi: ")
        return choice

    def get_players_id(self):
        players_id = []
        while len(players_id) < 8:
            id = input("Entrer l'id du joueur: ")
            if id not in players_id:
                players_id.append(id)
            else:
                print("Ce joueur a déjà été ajouté")
        return players_id

    def get_match_results(self, match):
        print(match[0][0], "VS", match[1][0])
        print("Qui a gagné le match ? \n1. Le joueur 1 a gagné \n2. Le joueur 2 a gagné \n3. Le match est nul")
        choice = input("Entrer votre choix: ")
        return choice
