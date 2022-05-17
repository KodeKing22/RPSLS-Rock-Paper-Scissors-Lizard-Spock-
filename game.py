import random
import winsound
from player import Player
from human import Human
from ai import Ai

class Game:

    def __init__(self):
        self.player_one= Human(input("Please input player name"))
        self.player_two= None
    

    def display_welcome():
        print ('Welcome to RPSLS Rock, Paper, Scissors, Lizard, Spock!')
        print('\n')
    


    def display_rules():
    
        print('Each match will be best of three games\n''Use number key to enter your selection')
        print('Rock crushes Scissors\n Scissors cuts Paper\n Paper covers Rock\n Rock crushes Lizard\n Lizard poisons Spock\n Spock smashes Scissors\n Scissors decapitates Lizard\n Lizard eats Paper\n Paper disproves Spock\n Spock vaporizes Rock')

# Rock crushes Scissors 
# Scissors cuts Paper 
# Paper covers Rock 
# Rock crushes Lizard 
# Lizard poisons Spock 
# Spock smashes Scissors 
# Scissors decapitates 
# Lizard Lizard eats Paper
# Paper disproves Spock 
# Spock vaporizes Rock
    
    def comparing_gestures ():
        if self.player_one 'Rock':




    def run_game():
        display_welcome()
        display_rules()
        whos_playing()

       
    def whos_playing():
        one_player_game = input('Would you like to play the computer? y/n')
        if one_player_game == 'y':
            self.player_two = Ai(Player)
        elif one_player_game == 'n':
            self.player_two = Human(Player)
            
# User input on number of players