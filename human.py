from player import Player
class Human(Player):
    def __init__(self):
        super().__init__()
        
    def choose_gesture(self):

        return super().choose_gesture()
    def player_choice(self):
        selected_gesture = input("1 is Rock, 2 is Paper, 3 is Scissors, 4 is Lizard, 5 is Spock")
        if selected_gesture == '1':
            self.selected_gesture = self.gestures [0] 
        elif selected_gesture == '2':
            self.selected_gesture = self.gestures [1]
        elif selected_gesture == '3':
            self
