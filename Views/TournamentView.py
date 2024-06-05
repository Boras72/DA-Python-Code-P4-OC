# TournamentView
from rich.console import Console
from rich.table import Table
from time import sleep
from config import MAX_PLAYER_NUMBER


class TournamentView:
    """
    Gère l'affichage et les interactions avec l'utilisateur pour le tournoi.
    """
    def __init__(self):
        pass
        
    def create_tournament(self):
        """
        Création d'un tournoi.
        
        Args:
            name (str) : nom du joueur.
            location (str) : lieu du tournoi
            start_date (datetime.date) : date de début.
            end_date (datetime.date) : date de fin.
            description (str) : commentaire.
            
        Returns:
            str: Informations d'un tournoi.
        """
        
        name = input("Indiquez le nom du tournoi: ")
        start_date = input("Indiquez la date de début du tournoi: ")
        end_date = input("Indiquez la date de fin du tournoi: ")
        location = input("Indiquer le lieu du tournoi: ")
        description = input("Veuillez saisir un commentaire: ")
        return name, location, start_date, end_date, description

    def display_tournament(self, tournaments):
        table = Table(title="Liste des tournois")
        table.add_column("Id", style="white", no_wrap=True)
        table.add_column("Name", style="magenta")
        table.add_column("Location", justify="right", style="cyan")
        table.add_column("Start date", justify="right", style="blue")
        table.add_column("End date", justify="right", style="blue")
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
            table.add_column("Id", style="white", no_wrap=True)
            table.add_column("Name", style="magenta", no_wrap=True)
            table.add_column("Start time", style="blue", no_wrap=True)
            table.add_column("End time", style="blue", no_wrap=True)
            table.add_column("Status", style="green", no_wrap=True)

            status = "terminé" if round.end_time else "en cours"

            table.add_row(str(round.id), round.name, round.start_time, round.end_time, status)

            console.print(table)
            table = Table(title=f"Liste des matches du {round.name}")
            table.add_column("Player1", style="magenta", no_wrap=True)
            table.add_column("Score P1", style="cyan", no_wrap=True)
            table.add_column("Vs.", style="blue", no_wrap=True)
            table.add_column("Score P2", style="cyan", no_wrap=True)
            table.add_column("Player2", style="magenta", no_wrap=True)

            for match in round.matches:
                table.add_row(match[0][0], str(match[0][1]), "Vs", str(match[1][1]), match[1][0])
            console.print(table)

    def get_tournament_id(self):
        choice = input("Entrer l'identifiant du tournoi: ")
        return choice

    def get_players_id(self):
        players_id = []
        counter = 1
        while len(players_id) < MAX_PLAYER_NUMBER:
            id = input(f"Entrer l'id du joueur {counter}/{MAX_PLAYER_NUMBER}: ")
            if id not in players_id:
                players_id.append(id)
                counter += 1
            else:
                print("Ce joueur a déjà été ajouté")
        return players_id

    def get_match_results(self, match):
        print(match[0][0], "VS", match[1][0])
        print("Qui a gagné le match ? \n1. Le joueur 1 a gagné \n2. Le joueur 2 a gagné \n3. Le match est nul")
        choice = input("Entrer votre choix: ")
        return choice

    def next_step(self, state_number, round_number=1):
        console = Console()
        if state_number == 1:
            console.print("Le tournoi a été créé avec succès", style="green")
            print("Souhaitez-vous ajouter des joueurs au tournoi ?")

        elif state_number == 2 and round_number == 1:
            console.print("Les joueurs ont bien été ajoutés au tournoi", style="green")
            print("Souhaitez-vous démarrer le premier round ?")

        elif state_number == 2 and round_number != 1:
            console.print(f"Le round {round_number-1} est terminé", style="green")
            print(f"Souhaitez-vous démarrer le round {round_number} ?")

        elif state_number == 3:
            console.print(f"Les matches du round {round_number} sont terminés", style="green")
            print("Souhaitez-vous saisir les scores ?")

        choice = input("1. OUI | 2. NON: ")
        return choice

    def prepare_round(self):
        console = Console()

        data = [
            "Sélection des joueurs",
            "Création des matches",
            "Déroulement des matches",
            "Les matches sont terminés!",
        ]
        while data:
            text = data.pop(0)
            sleep(1)
            console.log(f"[green]{text}[/green]")
            console.log("[bold][red]Round terminé!")
