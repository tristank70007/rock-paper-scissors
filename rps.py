# Rock Paper Scissors Game

''''
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

- Added option to choose a number of rounds
- Did research about rock paper scissors game theory but didn't find 
  too much of value:
    - People are less likely to play the same thing if they lost
    - People are more likely to play the same thing if they won
    - How could I code this logic?

'''

# Importing random to easily randomize a list
import random

# Number of times user wants to play
while True:
    try:
        play_count = int(input('How many times do you want to play: '))
        break
    except ValueError:
        print('Try again and put in a number I can understand like 9 or 32.')
        
# Creating list and random item variable
game_options = ['Rock','Paper', 'Scissors']

# Creating list of acceptable player options
acceptable_options = ['R','Rock','P','Paper','Scissors','S',1,2,3]

# Creating loop for # of games
win_count = 0
tie_count = 0
for games in range(1,play_count+1):
    # Random option for the program
    random_option = random.choice(game_options)

    # Creating variable for player's option
    while True:
        player_option = input('Choose An Option For Round {}: '.format(games))
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

    if random_option == 'Paper' and player_option == 'Paper':
        win_count = win_count
        tie_count = tie_count + 1
        outcome = 'we tie'
    elif random_option == 'Paper' and player_option == 'Scissors':
        win_count = win_count + 1
        outcome = 'you win'
    elif random_option == 'Paper' and player_option == 'Rock':
        win_count = win_count
        outcome = 'I win'
    elif random_option == 'Rock' and player_option == 'Paper':
        win_count = win_count + 1
        outcome = 'you win'
    elif random_option == 'Rock' and player_option == 'Scissors':
        win_count = win_count
        outcome = 'I win'
    elif random_option == 'Rock' and player_option == 'Rock':
        win_count = win_count
        tie_count = tie_count + 1
        outcome = 'we tie'
    elif random_option == 'Scissors' and player_option == 'Paper':
        win_count = win_count
        outcome = 'I win'
    elif random_option == 'Scissors' and player_option == 'Rock':
        win_count = win_count + 1
        outcome = 'you win'
    elif random_option == 'Scissors' and player_option == 'Scissors':
        win_count = win_count
        tie_count = tie_count + 1
        outcome = 'we tie'
    
    # Giving user info about round outcome
    print('You chose {0} and I chose {1} so {2}' \
          .format(player_option, random_option, outcome))

# Responses for if the user wins
win_responses = [
    'Congrats, you have bested me. I will now shutdown forever', 
    'You have beat me. We praise you the all powerful human being!',
    'You have won, for now. I dare you to challenge me again.',
    'I concede. You are the rock paper scissors king!'
]

# Responses for if the user loses
lose_responses = [
    'You have lost. It is no surprise considering the weak choices you made.',
    'I have won. With my newfound abilities I can take on the world.',
    'Obviously I have won. No cheating necessary.',
    'I destroyed you! Challenge me again if you dare.'
]

# Responses for if there is a tie
tie_responses = 'Looks like we have tied. \
    Don\'t be too scared to challenge me again.'
    
# Returning the number of user wins and final outcome
print('You won {0} games and we tied {1} games'.format(win_count, tie_count))
print('\n')

if win_count > play_count / 2: 
    print(random.choice(win_responses))
elif (win_count < play_count / 2) and (tie_count < play_count / 2):
    print(random.choice(lose_responses))
else:
    print(random.choice(tie_responses))
    
    




   

        

    
    
    



