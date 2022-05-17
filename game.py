import random
from player import Player
from human import Human
from ai import Ai


gesture = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']


class Game():
    def __init__(self):
        self.player_one= Human( )
        self.player_two= None

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.whos_playing()
        self.comparing_gestures()


    def whos_playing(self):
        self.player_one = Human()
        one_player_game = input('Do you want to play the computer:y/n   ')
        if one_player_game == 'y':
            self.player_two = Ai()
        elif one_player_game == 'n':
            self.player_two = Human()
    

    def display_welcome(self):
        print ('Welcome to RPSLS Rock, Paper, Scissors, Lizard, Spock!')
        print('\n')
    


    def display_rules(self):
    
        print('Each match will be best of three games\n''Enter: Rock, Paper, Scissors, Lizard or Spock .')
        print('Rock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock')

    def player_choice(player):
        player.player_one_choice = Human(input('Please make a gesture selection. '))
        player.player_two_choice = Human(input('Please make a gesture selection'))

    def ai_choice(player):
        player.player_two_choice = random.choice(gesture)
        variable_one = player.player_two_choice
        print(variable_one)

    def comparing_gestures (self):
        while self.player_one.score <2 and self.player_two.score <2 :
            self.player_one.choose_gesture()
            self.player_one.selected_gesture
            self.player_one.player_choice()
            self.player_two.player_choice()
            if self.player_one_choice == 'Rock' and self.player_two_choice == 'scissors' or 'lizard':
                print('Player One wins!')
                self.player_one = (self.player_one.score)
            elif self.player_one_choice == 'Paper' and self.player_two_choice == 'Rock' or 'Spock':
                print('Player one win!')
                self.player_one = (self.player_one.score)
            elif self.player_one_choice == 'Scissors' and self.player_two_choice == 'Paper' or 'Lizard':
                print('Player one win!')
                self.player_one = (self.player_one.score)
            elif self.player_one_choice == 'Lizard' and self.player_two_choice == 'Paper' or 'Spock':
                print('Player one win!')
                self.player_one = (self.player_one.score)
            elif self.player_one_choice == 'Spock' and self.player_two_choice == 'Rock' or 'Scissors':
                print('Player one win!')
                self.player_one =  (self.player_one.score)
            elif self.player_one_choice == self.player_two_choice:
                print('Tied')    
        else:
            print ('Player Two wins!')
            self.player_two = (self.player_two.score +1)



 

   
       
   
            
