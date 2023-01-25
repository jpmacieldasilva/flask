from .Team import Team
from .List import List


class Teams(List, Team):
    def __init__(self, num_players=5):
        super().__init__()
        self.team1 = Team()
        self.team2 = Team()
        self.num_players = num_players
        self.avaliables = [player["name"]
                           for player in self.players if player.get("avaliable") == True]

    def team1_players(self):
        return f'{self.team1.players}'

    def team2_players(self):
        return f'{self.team2.players}'

    def set_teams(self):
        if len(self.avaliables) >= self.num_players*2:
            self.team1.players = self.avaliables[:self.num_players]
            del self.avaliables[:self.num_players]
            self.team2.players = self.avaliables[:self.num_players]
            del self.avaliables[:self.num_players]
        else:
            return 'No players avaliables'

    def change_team(self, team_num):
        if team_num == "team1":
            self.avaliables += self.team1.players
            self.team1.players = []
            self.team1.players = self.avaliables[:self.num_players]
            del self.avaliables[:self.num_players]
        elif team_num == "team2":
            self.avaliables += self.team2.players
            self.team2.players = []
            self.team2.players = self.avaliables[:self.num_players]
            del self.avaliables[:self.num_players]

    def change_player(self, player_name):
        team_selected = None
        if player_name in self.team1.players:
            team_selected = self.team1.players
        elif player_name in self.team2.players:
            team_selected = self.team2.players

        if team_selected:
            team_selected.remove(player_name)
            self.set_avaliable(player_name)
            new_player = self.avaliables[0]
            team_selected.append(new_player)
            del self.avaliables[0]
        else:
            self.set_avaliable(player_name)
            print("Não tava nos times")
