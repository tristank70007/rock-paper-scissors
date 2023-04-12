# Rock Paper Scissors Game

""""
Writing it out so I can talk myself through what I need to do:

Main task is take one of three inputs from user and put it against
one of the same three options randomly. I would like to give some flexibility
when it comes to the inputs. (lowercase or titlecase, a number paired to
the option e.g. 1: Rock ) I would also like to make sure they are putting in
a valid option my program will be able to accept.

Extras: Want to give the user an option to play a number of rounds and see
who wins the most. Want to add some time delays to the code so it feels a 
bit nicer to interact with (more conversational). Want to see if there is
some facts about what wins most often to try to give the program an edge.

"""

# Importing random to easily randomize a list
import random

# Number of times user wants to play
while True:
    try:
        play_count = int(input('How many times do you want to play: '))
        break
    except ValueError:
        print('Try again and choose a number')
        
# Creating list and random item variable
game_options = ['Rock','Paper', 'Scissors']

random_option = random.choice(game_options)


# Creating variable for player's option
acceptable_options = ['R','Rock','P','Paper','Scissors','S',1,2,3]

while True:
    player_option = input('Choose An Option: ')
    if type(player_option) == str:
        player_option = player_option.title()
    
    if player_option in acceptable_options:
        print('Good choice')
        break
    else:
        print('Try again')
        

# Giving player option one of three values
if player_option in ['Rock','R',1]:
    player_option = 'Rock'
elif player_option in ['P','Paper',2]:
    player_option = 'Paper'
else:
    player_option = 'Scissors'
    
# Playing the game
win_count = 0
tie_count = 0
for games in range(1,play_count):
    if random_option == 'Paper' and player_option == 'Paper':
        win_count = win_count
        tie_count = tie_count + 1
    elif random_option == 'Paper' and player_option == 'Scissors':
        win_count = win_count + 1
    elif random_option == 'Paper' and player_option == 'Rock':
        win_count = win_count
    elif random_option == 'Rock' and player_option == 'Paper':
        win_count = win_count + 1
    elif random_option == 'Rock' and player_option == 'Scissors':
        win_count = win_count
    elif random_option == 'Rock' and player_option == 'Rock':
        win_count = win_count
        tie_count = tie_count + 1
    elif random_option == 'Scissors' and player_option == 'Paper':
        win_count = win_count
    elif random_option == 'Scissors' and player_option == 'Rock':
        win_count = win_count + 1
    elif random_option == 'Scissors' and player_option == 'Scissors':
        win_count = win_count
        tie_count = tie_count + 1

print("You won {} games".format(win_count))
    
    




   

        

    
    
    



