#Task 1: Random Choice Game Create a game where a player has a list of items.
#They have to guess which item in the list was selected.
#Use random.choice() to select the item and take the user's guess via input.
#Provide feedback on whether they guessed correctly or not keep them playing until they guess correctly.

import random

items = ['headphones', 'pillow', 'the creature', 'keys', 'candy', 'water bottle', 'laptop', 'pen', 'apple', 'pineapple', 'pineapple pen']

selected = (random.choice(items))

print('The following items are present with us. ')
print(items)
print('One item from these has been selected at random.')
while True:
    selection = input('Which do you think it is? ')
    if selection == selected:
        print("That was it! Congratulations!")
        break
    else:
        print("Sorry, that wasn't it. Try again! ")