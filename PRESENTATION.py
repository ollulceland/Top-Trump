import random
import requests
from time import sleep

# these are the beginning scores and the round number.

computer_score = 0
person_score = 0
rounds = 1

# This is the opening text that explains the game to the player
print('A long time ago in a galaxy far, far away....') ; sleep(3)
print('A top trumps game has begun to defeat the evil Computer Empire...') ; sleep(3)
print('You will be dealt 3 cards. Pick your strongest card and stat') ; sleep(2)
print('The Computer Empire will then choose a card') ;  sleep(2)
print('The player with the highest stat wins!') ; sleep(2)
print('You must win three rounds to defeat the Computer Empire!') ; sleep(2)
print('MAY THE FORCE BE WITH YOU!') ; sleep(2)

#Randomised flavour text to create fight sentances later on in the game, more exciting!

while True:
    verbs = ['smashes into', 'burns a hole in', 'fires its lasers at', 'tears apart', 'explodes', 'vaporises',
             'strikes', 'bombards', 'attacks', 'crushes', 'wrecks', 'decimates', 'destroys', 'shatters']
    nouns = ['the hull of', 'the wings of', 'the cockpit of', 'the cargo bay of', "the crew's quarters of",
             'the shields of', 'the rocket thrusters of', 'the medbay of', 'the cloning chambers of', 'the engine room of']
    sentence = random.choice(verbs) + " " + random.choice(nouns)

    print("******************* ROUND #", rounds, "*******************") ; sleep(1)


    # this is the code that offers the player 3 random cards

    seq_test = [2, 3, 5, 9, 10, 11, 12, 13, 15, 17, 21, 22, 23, 27, 28, 29, 31, 32]

    #function to extract data from API and return as dictionary
    #used random.choice instead of randm.randint as {'detail':'Not found'} error message for certain id numbers


    def card_select():
        starwars_id = random.choice(seq_test)
        url = 'https://swapi.dev/api/starships/{}/'.format(starwars_id)
        response = requests.get(url)
        starwars = response.json()

        # print(starwars["count"] output gives the number of characters in the starwars API, thanks Vanessa!
        return {
            "name": starwars["name"],
            "max_atmosphering_speed": starwars["max_atmosphering_speed"],
            "length": starwars["length"],
            "crew": starwars["crew"],

        }

    Dealt_hand = [card_select(), card_select(), card_select()]


    for e, c in enumerate(Dealt_hand):
        print('{} Name: {}'.format(e, c['name']))
        print('Max_atmosphering_speed: {} '.format(c['max_atmosphering_speed']))
        print('Length: {} '.format(c['length']))
        print("Crew: {} ".format(c['crew'])) ;sleep(2)
        print('   ')

    # This lets the player pick the card they want to play with

    card_chosen = input('Which card do you choose to play with? 0-2: ')
    if card_chosen == '0':
        player_card = Dealt_hand[0]
    elif card_chosen == '1':
        player_card = Dealt_hand[1]
    elif card_chosen == '2':
        player_card = Dealt_hand[2]
    else:
        print("Sorry that selection was invalid. Enter a value in the range")

    print('You have chosen: {}'.format(player_card['name']))

    # this section lets the player choose a stat

    sleep(1)
    print("    ")

# if statements to determine which stat is used depending on user input

    chosen_stat = input('Which stat from this card do you choose to play with?: ')
    if chosen_stat == 'max_atmosphering_speed':
        user_stat = player_card['max_atmosphering_speed']
        print('You have a stat of {}'.format(user_stat))
        sleep(1)
    elif chosen_stat == 'length':
        user_stat = player_card['length']
        print('You have a stat of {}'.format(user_stat))
        sleep(1)
    elif chosen_stat == 'crew':
        user_stat = player_card['crew']
        print(user_stat)
    else:
        print('Please can you type the exact name of the stat, all lower case')
        sleep(1)

    print("   ")

    # Comp chooses a card to play

    computer_card = card_select()
    print('The Computer Empire has chosen the {} card'.format(computer_card['name']))
    sleep(1)

    computer_stat = computer_card[chosen_stat]

    print('The Computer Empire has a stat of {}'.format(computer_stat))
    sleep(1)

    print("   ")

    # now the 2 stats are compared and a winner is determined. It also updates the score counter and the round counter.

    if computer_stat > user_stat:
        computer_score += 1
        rounds += 1
        print('The {} '.format(computer_card['name']) + sentence + " your {}".format(player_card['name']))
        sleep(3)
        print('     ')
        print('The Computer Empire won this round!') ; sleep(1)
        print('  ')

    elif user_stat > computer_stat:
        person_score += 1
        rounds += 1
        print('The {} '.format(player_card['name']) + sentence + " the Computer Empire's {}".format(computer_card['name']))
        sleep(3)
        print('   ')
        print('Well done you have won this round!') ; sleep(1)
        print('  ')

    else:
        rounds += 1

        print("The {}'s lasers harmlessly bounce off the shields of your {}".format(computer_card['name'], player_card['name']))
        sleep(2)
        print('   ')
        print('We have drawn this round') ; sleep(1)
        print('  ')

    print("Your score:", person_score) ; sleep(1)
    print("Computer's score:", computer_score) ; sleep(1)
    print("   ")

# these are the conditions for the end of the game and the messages for when the game ends.
    if person_score == 3:
        print("Congratulations on winning!!")
        print("You have defeated the evil Computer Empire!!!!")
        print("This is the end of the game.")
        break
    elif computer_score == 3:
        print("Oh no!")
        print("the Computer Empire has defeated you :(")
        print("This game is over, but you can always try again!")
        break
