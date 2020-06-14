"""First Homework. Some simple programmes to train Python style."""

# 1. 'Hello world-like' programme
print("Hi there, greetings from Maksim!")

# 2. Another simple programme asking to input your name and printing some
# text with the name from input
name = input("What's your name?\n")
print("Hi, %s! Glad to hear from you!" % name)

# 3. Prints friends' id and name from list using for-cycle
friends = ['john', 'pat', 'gary', 'michael']
for i, name1 in enumerate(friends):
    print('My friend {iteration} is {name}'.format(iteration=i, name=name1))

# 4. Fibonacci, tuple assignment.
# Prints number of babies in the next generation while number of babies do
# not exceeds 100
parents, babies = (1, 1)
while babies < 100:
    print ('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)
