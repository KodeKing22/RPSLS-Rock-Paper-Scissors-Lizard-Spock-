class Player:
    def __init__(self, player):
        self.name = player
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.selected_gesture = ''
        self.score = 0
    def choose_gesture(self):
        pass