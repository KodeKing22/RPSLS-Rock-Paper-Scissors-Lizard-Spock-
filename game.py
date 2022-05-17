import random
from player import Player

class Game:

    def __init__(self):


    def display_welcome():
        print ('Welcome to RPSLS Rock, Paper, Scissors, Lizard, Spock!')
        print('\n')
    


    def display_rules():
    
        print('Each match will be best of three games\n''Use number key to enter your selection')
        print('Rock crushes Scissors\n Scissors cuts Paper\n Paper covers Rock\n Rock crushes Lizard\n Lizard poisons Spock\n Spock smashes Scissors\n Scissors decapitates Lizard\n Lizard eats Paper\n Paper disproves Spock\n Spock vaporizes Rock')


    def number_to_name(number):
        if number == 0:
            return "rock"
        elif number == 1:
            return "Spock"
        elif number == 2:
            return "paper"
        elif number == 3:
            return "lizard"
        elif number == 4:
            return "scissors"
        else:
            return "Error"

    def name_to_number(name):
        if name == "rock":
            return 0
        elif name == "Spock":
            return 1
        elif name == "paper":
            return 2
        elif name == "lizard":
            return 3
        elif name == "scissors":
            return 4
        else:
            print name + "is not a character in RPSLS"


    def run_game():
        display_welcome()
        display_rules()
        whos_playing()

       
    def whos_playing():
        one_player_game = input('Would you like to play the computer? y/n')
        if one_player_game == 'y':
            human.player.one 
        elif one_player_game == 'n':
            human.player.two
            pass 
# User input on number of players