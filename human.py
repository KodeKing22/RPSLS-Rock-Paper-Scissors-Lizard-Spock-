from player import Player
# input
class Human(Player):
    def __init__(self):
        super(self).__init__()
        
    
    def player_choice(self):
        self.player_one = Human(input('Please make a gesture selection'))
        self.player_two = Human(input('Please make a gesture selection'))
        
