from .Teams import Teams
from .List import List
import time


class Game(Teams, List):
    def __init__(self):
        super().__init__()
        self.time_match = 5
        self.resultado = None
        self.minutes = 10
        self.paused = False
        self.finished = False
        self.time_min = '{:02d}'.format(self.minutes)
        self.time_sec = "00"

    def countdown(self):
        num_of_secs = self.minutes*3

        while num_of_secs and self.paused == False:
            min, sec = divmod(num_of_secs, 60)
            self.time_min = '{:02d}'.format(min)
            self.time_sec = '{:02d}'.format(sec)
            time.sleep(1)
            num_of_secs -= 1
        self.finished = True
        print('Countdown finished.')

    def pause(self):
        self.paused = True

    def play(self):
        self.paused = False
        self.countdown()

    def reset_timer(self):
        self.minutes = self.minutes
        self.paused = False
        self.finished = False

    @property
    def match(self):
        return self.set_teams

    @property
    def start_match(self):
        self.play()
        return "Começou!"

    def score(self, team):
        who_scored = team
        if who_scored == "team1":
            print("Gol do time 1")
            self.team1.score += 1
            self.resultado = None
        elif who_scored == "team2":
            print("Gol do time 2")
            self.team2.score += 1
            self.resultado = None

    def winner(self):
        winner = self.team1.score - self.team2.score
        self.resultado = None
        if winner > 0:
            self.resultado = "Equipe 1 venceu"
            self.change_team("team2")
            print(f"Equipe 2: {self.team2_players()}")
            self.team1.score = 0
            self.team2.score = 0
        elif winner < 0:
            self.resultado = "Equipe 2 venceu"
            self.change_team("team1")
            print(f"Equipe 1: {self.team1_players()}")
            self.team1.score = 0
            self.team2.score = 0
        elif winner == 0:
            self.resultado = "Empatou, sai os dois"
            self.change_team("team1")
            self.change_team("team2")
            print(f"Equipe 1: {self.team1_players()}")
            print(f"Equipe 2: {self.team2_players()}")
            self.team1.score = 0
            self.team2.score = 0

    def reset(self):
        self.team1.players = []
        self.team2.players = []
        self.team1.score = 0
        self.team2.score = 0
        self.resultado = None
        self.reset_timer()
        self.avaliables = []
        self.avaliables = [player["name"]
                           for player in self.players if player.get("avaliable") == True]
