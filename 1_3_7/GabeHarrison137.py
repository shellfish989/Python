# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt # standard short name
import random

plt.ion() # sets “interactive on”: figures redrawn when updated

def picks():
    a = [] # make an empty list

    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list      ]
    #    random.choice(   [brackets here to choose from a list] )
    # a += [random.choice([1, 3, 10])]

    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.show()
    
def roll_hundred_pair():
    

def days():
    ''' 
        The code will take every single letter in the string 'day' and put it right before the word
        day, then takes all numbers between the range and says it's the blank day of september for
        all the numbers
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(21,22):
        print('Do you remember ' + str(day) + 'st night of September?')
        print('While chasing the clouds away. Our hearts were ringing')
        print('In the key that our souls were singing')
        print('As we danced in the night')
        print('Remember, how the stars stole the night away, yeah yeah yeah')
        print('Hey hey hey')
        print('Bada Ya, say do you remember')
        print('Bada Ya, dancing in September')
        print('Bada Ya, never was a cloudy day')
        print('Ba duda, ba duda, ba duda, badu')
        print('Ba duda, badu, ba duda, badu')
        print('Ba duda, badu, ba duda')
        print('My thoughts are with you')
        print('Holding hands with your heart to see you')
        print('Only blue talk and love')
        print('Remember, how we knew love was here to stay')
        print('Now December found the love that we shared in September')
        print('Only blue talk and love')
        print('Remember, the true love we share today')
        print('Hey hey hey')
        print('Bada Ya, say do you remember')
        print('Bada Ya, dancing in September')
        print('Bada Ya, never was a cloudy day')
        print('Ba duda, ba duda, ba duda, badu')
        print('Ba duda, badu, ba duda, badu')
        print('Ba duda, badu, ba duda')
        print('There was a')
        print('Bada Ya, say do you remember')
        print('Bada Ya, dancing in September')
        print('Bada Ya, never was a cloudy day')
        print('Ba duda, ba duda, ba duda, badu')
        print('Ba duda, badu, ba duda, badu')
        print('Ba duda, badu, ba duda')
        print('The bell was ringing')
        print('Our souls were singing')
        print('Do you remember every cloudy day')
        print('There was a')
        print('Bada Ya, say do you remember')
        print('Bada Ya, dancing in September')
        print('Bada Ya, never was a cloudy day')
        print('Ba duda, ba duda, ba duda, badu')
        print('Ba duda, badu, ba duda, badu')
        print('Ba duda, badu, ba duda')
        print('And well say')
        print('Bada Ya, say do you remember')
        print('Bada Ya, dancing in September')
        print('Bada Ya, never was a cloudy day')
        print('Ba duda, ba duda, ba duda, badu')
        print('Ba duda, badu, ba duda, badu')
        print('Ba duda, badu, ba duda')
        