from secrets import choice
from player import Player
import random   

class Ai(Player):
    def __init__(player):
        super(). __init__

    def choose_gesture(self):
        selected_gesture = random.choice(self.gestures)
        if selected_gesture == '1':
            self.selected_gesture = self.gestures [0] 
        elif selected_gesture == '2':
            self.selected_gesture = self.gestures [1]
        elif selected_gesture == '3':
            self.selected_gesture = self.gestures [2]
        elif selected_gesture == '4':
            self.selected_gesture = self.gestures [3]
        elif selected_gesture == '5':
            self.selected_gesture = self.gestures [4]
     
        