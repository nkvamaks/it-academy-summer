"""First Homework. Some simple programmes to train Python style."""

print("Hi there, greetings from Maksim!")

name = input("What's your name?\n")
print("Hi, %s! Glad to hear from you!" % name)

friends = ['john', 'pat', 'gary', 'michael']
for i, name1 in enumerate(friends):
    print('My friend {iteration} is {name}'.format(iteration=i, name=name1))
