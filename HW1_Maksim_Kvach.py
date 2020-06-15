"""Homework 1. Some Simple Programmes to Practice Python Style."""
import re
import random
from time import localtime


""" 1. 'Hello world-like' programme"""
print("Hi there, greetings from Maksim!")


""" 2. Another simple programme asking to input your name and printing some
text with the name from input."""
name = input("What's your name?\n")
print("Hi, %s! Glad to hear from you!" % name)


""" 3. Prints friends' id and name from list using for-cycle."""
friends = ['john', 'pat', 'gary', 'michael']
for i, name1 in enumerate(friends):
    print('My friend {iteration} is {name}'.format(iteration=i, name=name1))


""" 4. Fibonacci, tuple assignment.
Prints number of babies in the next generation while number of babies do
not exceeds 100."""
parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)


""" 5. Functions."""


def greet(name):
    """Greetings.

    Defines a simple function taking a 'name' as an argument and returns
    greetings
    """
    print('Hello', name)


greet('Jack')
greet('Jill')
greet('Bob')


"""Import, regular expressions.
Tests string as a valid US local phone number using regular expressions.
"""
for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print(test_string, 'is a valid US local phone number')
    else:
        print(test_string, 'rejected')


"""Dictionaries, generator expressions.
Calculates total sum of purchases using Dictionaries that store items and
prices, and generator expressions for calculations.
"""
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {'apple': 1, 'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print('I owe the grocer $%.2f' % grocery_bill)


"""Triple-quoted strings, while loop.
Prints lovely piece of poetry with quite simple pythonic code."""
REFRAIN = '''
%d bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!
'''
bottles_of_beer = 9
while bottles_of_beer > 1:
    print(REFRAIN % (bottles_of_beer, bottles_of_beer,
          bottles_of_beer - 1))
    bottles_of_beer -= 1


"""Time, conditionals, from..import, for..else """
activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting'}

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print(activities[activity_time])
        break
else:
    print('Unknown, AFK or sleeping!')


""""Guess the Number" Game (edited) from http://inventwithpython.com"""
guesses_made = 0
name = input('Hello! What is your name?\n')

number = random.randint(1, 20)
print('Well, {0}, I am thinking of a number between 1 and 20.'.format(name))

while guesses_made < 6:
    guess = int(input('Take a guess: '))
    guesses_made += 1
    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break

if guess == number:
    print('Good job, {0}! You guessed my number '
          'in {1} guesses!'.format(name, guesses_made))
else:
    print('Nope. The number I was thinking of was {0}'.format(number))
