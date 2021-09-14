import random
import requests
from time import sleep

#writing the file to strore the users score
with open('score_keeperU.txt', 'w+') as text_file:
    tally = ('')
    text_file.write(tally)

#writing the file to store the computers score
with open('score_keeperC.txt', 'w+') as text_file:
    tally = ('')
    text_file.write(tally)
#I think these files may contain tuples not lists

#function to edit the users score file
def score_editorU(x):
    with open('score_keeperU.txt', 'r') as score_file:
        score = score_file.read()
    added = x
    score = score + added + '\n'
    with open('score_keeper1.txt.txt', 'w+') as score_file:
        score_file.write(score)
        print('You currently have a score of:')
        print(score)


def score_editorC(x):
    with open('score_keeperC.txt', 'r') as score_file:
        score = score_file.read()
    added = x
    score = score + added + '\n'
    with open('score_keeper1.txt.txt', 'w+') as score_file:
        score_file.write(score)
        print('I currently have a score of:')
        print(score)
#The print statement in the fucntion would not allow me to use .format






def card_select():
    id_number = random.randint(1, 151)
    url = 'http://pokeapi.co/api/v2/pokemon/{}/'.format(id_number)
    response = requests.get(url)
    card = response.json()

    return {
        'name': card['name'],
        'id': card['id'],
        'height': card['height'],
        'weight': card['weight'],
    }


Dealt_hand = [card_select(), card_select(), card_select(), card_select()]


for e, c in enumerate(Dealt_hand):
    print('{} Name: {}'.format(e, c['name']))
    print(' ID: {} '.format(c['id']))
    print('Height: {} '.format(c['height']))
    print("""Weight: {}
     ...""".format(e, c['weight']))

card_chosen = input('Which card do you choose to play with? 0-3: ')
if card_chosen == '0':
    player_card = Dealt_hand[0]
elif card_chosen == '1':
    player_card = Dealt_hand[1]
elif card_chosen == '2':
    player_card = Dealt_hand[2]
elif card_chosen == '3':
    player_card = Dealt_hand[3]

print('You have chosen: {}'.format(player_card['name'])) ; sleep(1)
chosen_stat = input('Which stat from this card do you choose to play with?: ')
if chosen_stat == 'id':
    user_stat = player_card['id']
    print('You have a stat of {}'.format(user_stat)) ; sleep(1)
elif chosen_stat == 'height':
    user_stat = player_card['height']
    print('You have a stat of {}'. format(user_stat)) ; sleep(1)
elif chosen_stat == 'weight':
    user_stat = player_card['weight']
    print(user_stat)
else:
    print('Please can you type the exact name of the stat, all lower case') ;sleep(1)
computer_card = card_select()
print('I am using the {} card'.format(computer_card['name'])) ; sleep(1)


computer_stat = computer_card[chosen_stat]

print('I have a stat of {}'.format(computer_stat)) ; sleep(1)

def who_wins():
    if computer_stat > user_stat:
        print('I have won this round!')
        score_editorC('1')
    elif computer_stat < user_stat:
        print('Well done you have won this round!')
        score_editorU('1')
    else:
        print('We have drawn this round')

who_wins()
