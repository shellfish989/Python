from __future__ import print_function
import random

def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess < secret:
        print ('Too low, my number is ', secret, '.', sep='')
    if guess > secret:
        print ('Too high, my number is ', secret, '.', sep='')
    else:
        print('Right, my number is', guess, end='!\n')

def food_id(food):
    ''' Returns categorization of food
    
    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']
    
    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, fruit'
        else:
            return 'NOT citrus, fruit'
    else:
        if food in starchy:
            return 'Startchy, NOT a fruit'
        else:
            return 'NOT starchy, NOT a fruit'
        
def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = False
        print('orange bug in food id()')
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = False
        print ('banana bug in food id()')
    if food_id('apple') != 'NOT Citrus, Fruit':
        works = False
        print('apple bug in food id()')
    if food_id('potato') != 'Startchy, NOT a Fruit':
        works = False
        print ('potato bug in food id()')
    if works:
        print('food_id_passed all tests')
def f(n):
    if int(n) == n:
        if n % 2 == 0:
            if n % 3 == 0:
                print ('That is a multiple of 6')
            else:
                print ('That is an even number')
        else:
            print ('That is not an even integer')    
    else:
        print ('That is not an integer')
        
def quiz_decimal(entry1, entry2):
    print ('enter a number between', entry1, 'and', entry2)
    guess = int(raw_input('Guess: '))
    if guess<entry1:
        print ('Wrong,', guess, 'is less than', entry1)
    if guess>entry2:
        print ('Wrong,', guess, 'is greater than', entry2)
    else:
        if entry1<guess<entry2:
            print ('that is correct')
       