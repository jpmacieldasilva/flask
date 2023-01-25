class List():
    def __init__(self):
        self.error = None
        self.sucess = None
        self.players = [{'name': '1', 'avaliable': True},
                        {'name': '2', 'avaliable': True},
                        {'name': '3', 'avaliable': True},
                        {'name': '4', 'avaliable': True},
                        {'name': '5', 'avaliable': True},
                        {'name': '6', 'avaliable': True},
                        {'name': '7', 'avaliable': True},
                        {'name': '8', 'avaliable': True},
                        {'name': '9', 'avaliable': True},
                        {'name': '10', 'avaliable': True},
                        {'name': '11', 'avaliable': True},
                        {'name': '12', 'avaliable': True},
                        {'name': '13', 'avaliable': True},
                        {'name': '14', 'avaliable': True},
                        {'name': '15', 'avaliable': True},
                        {'name': '16', 'avaliable': True},
                        {'name': '17', 'avaliable': True}]

    def add_player(self, name):
        if any(player["name"].capitalize() == name.capitalize() for player in self.players):
            self.error = "Player already exists."
            self.sucess = None
            return self.error
        else:
            self.players.append({"name": name, "avaliable": False})
            self.sucess = ("Player added.")
            self.error = None

    def remove_player(self, name):
        self.players = [
            player for player in self.players if player["name"] != name]
        print("Player removed.")

    def set_avaliable(self, name):
        player = next(
            (player for player in self.players if player["name"] == name), None)
        if player:
            player['avaliable'] = not player['avaliable']
        else:
            print(f'Player {name} not found')
