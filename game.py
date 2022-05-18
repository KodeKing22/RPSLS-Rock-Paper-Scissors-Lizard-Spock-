import random
from player import Player
from human import Human
from ai import Ai


# gesture = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']


class Game():
    def __init__(self):
        self.player_one= Human( )
        self.player_two= None

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.whos_playing()
        self.game_play()
        self.comparing_gestures()


    def whos_playing(self):
        self.player_one = Human()
        one_player_game = input('Do you want to play the computer? Y/N: ')
        if one_player_game == 'Y':
            self.player_two = Ai()
        elif one_player_game == 'N':
            self.player_two = Human()
    

    def display_welcome(self):
        print ('Welcome to RPSLS Rock, Paper, Scissors, Lizard, Spock!')
        print('\n')
    


    def display_rules(self):
    
        print('Each match will be best of three games')
        print('The rules are as follows:')
        print('Rock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock')
        print('\nMake a selection: Rock, Paper, Scissors, Lizard or Spock')

    def game_play(self):
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        
        self.player_one.selected_gesture = input('Whats your selection? ')
        input() != self.gestures
        print('Error not a gesture')
        print('Player 1 selected: ' + self.player_one.selected_gesture)
        self.player_two.selected_gesture = random.choice(self.gestures)
        print('Player 2 Selected: ' + self.player_two.selected_gesture)

    def comparing_gestures (self):
        self.player_one.choose_gesture()
        self.game_play()
        self.player_one.selected_gesture
        self.player_two.selected_gesture  
        
        while self.player_one.score <2 and self.player_two.score <2 :
                self.game_play()
                           
        if      self.player_one.selected_gesture == 'Rock'and self.player_two.selected_gesture == 'scissors' or 'lizard':
                print('Player one 1!')
        elif  self.player_one.score <2 and self.player_two.score <2 :
                self.player_one.selected_gesture = input('Whats your selection?  ')
                print('You selected: ' + self.player_one.selected_gesture)
        elif    self.player_one.selected_gesture == 'Rock' and self.player_two.selected_gesture == 'scissors' or 'lizard':
                self.player_one.score += 1
                print('Player one 2!') 
                self.player_one = (self.player_one.score)
        elif    self.player_one.selected_gesture == 'Paper' and self.player_two.selected_gesture == 'Rock' or 'Spock':
                self.player_one.score += 1
                print('Player one win!')
                self.player_one = (self.player_one.score)
        elif self.player_one.selected_gesture == 'Scissors' and self.player_two.selected_gesture == 'Paper' or 'Lizard':
                print('Player one win!')
                self.player_one = (self.player_one.score)
        elif self.player_one.selected_gesture == 'Lizard' and self.player_two.selected_gesture == 'Paper' or 'Spock':
                print('Player one win!')
                self.player_one = (self.player_one.score)
        elif self.player_one.selected_gesture == 'Spock' and self.player_two.selected_gesture == 'Rock' or 'Scissors':
                print('Player one win!')
                self.player_one =  (self.player_one.score)
        elif self.player_one.selected_gesture == self.player_two.selected_gesture:
                print('Tied')    
        else:
            print ('Player Two wins!')
            self.player_two = (self.player_two.score +1)
    



 

   
       
   
            
