''' The game sixteen is dead '''

__author__ = "Elemele, Qako"

import liste_numbers  # Import of the first module file .py.
import random
import time

print('''Hello there! You can start the game "Sixteen is dead"
All of the instructions and valid input possibilities are displayed over the course
 of the game!!! For further information please view the documentation. Good luck
 on your game!!!''')
players = []
while True:
    name_with_boolean = []  
    name = input('Please enter your name: ')
    name_with_boolean.append(name)
    boolean_choice = input(' Type in "yes" for real player or "no" for CPU: ')
    if boolean_choice == 'yes':  # Adds true, false to the list, along with name of the player depending on the answer.
        name_with_boolean.append(True)
    elif boolean_choice == 'no':
        name_with_boolean.append(False)
    else:  # If any other answer apart from ja or nein is given.
        print('Input invalid. Please enter yes or no and enter your name!!!')
        continue
    players.append(name_with_boolean)
    ask_for_players = input(' Enter "1" if another player wants to participate. Notice that the pressing of any other key lets the game start')
    if ask_for_players == '1':  # Option to enter more players.
        continue
    else:  # The game will start with the selected players.
        break
print(players)


def sixteen_is_dead(players):
    ''' Entire game

        :param players:  describes list of players

    '''
    dice_number_player = []
    score = 0
    players_turn = 0
    for n in players:  # For each loop, get the names from the list and start with the first element(0 in list).
        players[players_turn][0]
        print('Spieler ' + players[players_turn][0] + ' ist dran!!!')
        if n[1] == True:   # Checking the second element in the list(either true or false).
            while score <= 16:             
                dice = input(
                    'How many times do you want to roll the dice to get close to 16?: ')
                span_numbers = input(
                    'How many faces should your dice have?: ')
                if dice.isalpha() == True or span_numbers.isalpha() == True:
                    print('invalid input')
                    continue
                if dice == '' or span_numbers == '':
                    print('invalid input')
                    continue
                achieved_number = liste_numbers.roll_dice(
                    int(dice), int(span_numbers))  # Here we get the achieved number.
                rolled_number = sum(achieved_number)  # Variable that sums up the values of achieved numbers.
                score += int(rolled_number)  # Adds the value and the variable and assigns the result to the variable score. 
                if score == 9:
                    print('You have scored the following number: ' + str(score))
                    print('You are not allowed to roll the dice again, it is the next players turn')
                    break
                elif score == 10:
                    print('You have scored the following number: ' + str(score))
                    print('It is your turn again')
                    time.sleep(3)   # Stop the program for 3 seconds.
                    continue
                elif score >= 16:
                    print('You have scored the following number: ' + str(score))
                    print('YOU LOSE')
                    break
                elif score < 16 and score != 9:
                    print('You have scored the following number: ' + str(score))
                    choice = input(
                        'Do you want to roll the dice again? Please press enter if yes and "n" if not: ')
                    if choice == '':
                        continue
                    elif choice != '' and choice != 'n':
                        print('invalid input is equivalent to pressing enter')
                    elif choice == 'n':
                        print('the next player will roll')
                        break
                elif score >= 16:
                    print('You have reached 16 and you lose')
        elif n[1] == False:  # If the Element is false the computer plays.
            print('Players ' + players[players_turn][0] + 'turn and the player is a CPU!!!')
            score = 0
            choice_cpu = ['', 'n']  # Two choices in list(enter and n).
            while score <= 11:
                rolled_number_cpu = sum(liste_numbers.roll_dice())
                score += int(rolled_number_cpu)  # Adds the value and the variable and assigns the result to variable score.
                if score == 9:
                    print('CPU has reached the following score ' + str(score))
                    print('CPU can not roll the dice again')
                    break
                elif score == 10:
                    print('Computer has reached the following score ' + str(score))
                    print('CPU needs to roll the dice again')
                    time.sleep(3) 
                    continue
                elif score >= 16:
                    print('CPU has reached the following score ' + str(score))
                    print('CPU LOST')
                    break
                elif score >= 12 :
                    if random.choice(choice_cpu) == '': 
                        print('CPU rolls again')
                        time.sleep(3)
                        continue
                    elif random.choice(choice_cpu) == 'n':
                        print('CPU leaves the turn to the next player')
                        break
                elif score >= 16:
                    print('CPU lost')
                    break
        print('Player ' + players[players_turn][0] + 'has scored the following: ' + str(score))
        if score < 16 or score == 9:
            dice_number_player.append(score)  # This adds the score of achieved points to the list.
            score = 0
            players_turn += 1   # The next player plays.
        elif score >= 16:
            dice_number_player.append(score)
            break
        print(dice_number_player)
    least_achieved = dice_number_player.index(min(dice_number_player))  # Gets the index of the (least_achieved) in list.
    score_over_sixteen = dice_number_player.index(max(dice_number_player))  # Gets the index of the (score_over_sixteen) in list.
    
    if dice_number_player.count(min(dice_number_player)) == 1:  # Checks the number of repeated times of least_achieved.
        if max(dice_number_player) < 16:
            print('Player ' + players[least_achieved][0] + 'LOST') # Prints which player lost.
            print('And Player ' + players[score_over_sixteen][0] + ' WON')
        else:
            score_over_sixteen = dice_number_player.index(max(dice_number_player))
            print('Player ' + players[score_over_sixteen][0] + ' LOST')
    else:
        print('More than one player has reached the number: ' + str(min(dice_number_player)))
        print('there is no definite Loser')
        if dice_number_player.count(max(dice_number_player)) > 1:
            print(
                'There is no definite winner due to multiple players achieving the number:  ' + str(max(dice_number_player)))
        elif max(dice_number_player) < 16:
            print('However, Player ' + players[score_over_sixteen][0] + 'has won the game')
        

    newgame = input('Do you want to start a new round? Please enter "ja" if so and press enter if you want to end the game: ')
    if newgame == 'ja':
        print(sixteen_is_dead(players))  # The game will be executed again.
    elif newgame == '':  
        print(
            'The game ends. You can always start a new game by entering "sixteen_is_dead(players)"  '
            'in the shell')

sixteen_is_dead(players)  # The start of the game
