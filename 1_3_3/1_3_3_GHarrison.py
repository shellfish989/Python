from __future__ import print_function # use Python 3.0 printing

def age_limit_output(age):
    '''Step 6a if-else example'''
    AGE_LIMIT = 13 #convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(str(age) + ' is below the age limit.')
    else:
        print(str(age) + ' is old enough.')
    print('Minimum age is ' + str(AGE_LIMIT))
    
def report_grade_output(percent):
    '''Step 6b if-else'''
    GRADE_MINIMUM = 80
    if percent < GRADE_MINIMUM:
        print(str(percent) + ' does not show mastery, get help.')
    else:
        print(str(percent) + ' is good enough.')
    print('Minimum grade is ' + str(GRADE_MINIMUM))
def vowel(letter):
        vowels = 'aeiouAEIOU'
        if letter in vowels:
            return True
        else:
            return False
# should check len(letter)==1
def letter_in_word(guess, word):
    word = 'communism'
    if guess in word:
        return True
    else:
        return False
def hint(color, secret):
    if color in secret:
        True
        print(str(color) + ' is correct.')
    else:
        False
        print(str(color) + ' is wrong, get good.')