import random
import requests
from time import sleep

# these are the beginning scores and the round number.

computer_score = 0
person_score = 0
rounds = 1

print('A long time ago in a galaxy far, far away....') ; sleep(3)
print('A top trumps game has begun to defeat the evil computer empire...') ; sleep(3)
print('You will be dealt a hand of cards to pick and card and stat') ; sleep(2)
print('The computer empire with then choose a card') ;  sleep(2)
print('The player with the highest stat wins!') ; sleep(2)
print('You must win three rounds to defeat the computer empire!') ; sleep(2)
print('MAY THE FORCE BE WITH YOU!') ; sleep(2)

while True:
    print("******************* ROUND #", rounds, "*******************") ; sleep(1)



    # this is the code that offers the player 3 random cards

    def card_select():
        starwars_id = random.randint(1, 36)
        url = 'https://swapi.dev/api/starships/{}/'.format(starwars_id)
        response = requests.get(url)
        starwars = response.json()

        # print(starwars["count"] output gives the number of characters in the starwars API, thanks Vanessa!
        return {
            "name":starwars["name"],
            "max_atmosphering_speed":starwars["max_atmosphering_speed"],
            "length":starwars["length"],
            "crew":starwars["crew"],
        }

    card1 = card_select()
    card2 = card_select()
    card3 = card_select()


    Dealt_hand = [card1, card2, card3]


    for e, c in enumerate(Dealt_hand):
        print('{} Name: {}'.format(e, c['name']))
        print(' Speed: {} '.format(c['max_atmosphering_speed']))
        print('Length: {} '.format(c['length']))
        print("""Crew: {}
             ...""".format(e, c['crew'])) ;sleep(2)

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

    chosen_stat = input('Which stat from this card do you choose to play with?: ')
    if chosen_stat == 'Speed':
        user_stat = player_card['max_atmosphering_speed']
        print('You have a stat of {}'.format(user_stat));
        sleep(1)
    elif chosen_stat == 'Length':
        user_stat = player_card['length']
        print('You have a stat of {}'.format(user_stat)) ;
        sleep(1)
    elif chosen_stat == 'Crew':
        user_stat = player_card['crew']
        print(user_stat)
    else:
        print('Please can you type the exact name of the stat, all lower case');
        sleep(1)

    print("   ")

    # Comp chooses a card to play

    computer_card = card_select()
    print('The computer empire has chosen the {} card'.format(computer_card['name']));
    sleep(1)

    computer_stat = computer_card[chosen_stat]

    print('The computer empire has chosen {}'.format(computer_stat));
    sleep(1)

    print("   ")

    # now the 2 stats are compared and a winner is determined. It also updates the score counter and the round counter.

    if computer_stat > user_stat:
        computer_score += 1
        rounds += 1
        print('The computer empire won this round!')


    elif computer_stat < user_stat:
        person_score += 1
        rounds += 1
        print('Well done you have won this round!')


    else:
        rounds += 1
        print('We have drawn this round')

    print("Your score:", person_score)
    print("Computer's score:", computer_score)
    print("   ")
    sleep(2)

# these are the conditions for the end of the game and the messages for when the game ends.
    if person_score == 3:
        print("Congratulations on winning!!")
        print("You beat the computer!!!!")
        print("This is the end of the game.")
        break
    elif computer_score == 3:
        print("Oh no!")
        print("the computer empire beat you :(")
        print("This game is over, but you can always try again!")
        break




