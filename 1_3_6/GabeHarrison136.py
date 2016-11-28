import random
import string
random.choice(string.ascii_lowercase)
def roll_two_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print 'Your number is ', dice1 + dice2 ,''
def guess_letter():
    print random.choice(string.ascii_lowercase)