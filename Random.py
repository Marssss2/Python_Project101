import random

random.random
print(random.random())
random.randint
print(random.randint(1, 10)) # it will give you a random integer between 1 and 10 inclusive
random.choice
colors = ["red", "blue", "green", "yellow"]
print(random.choice(colors)) # it will randomly select one color from the list of colors
random.shuffle
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers) # it will shuffle the list of numbers in place, meaning that the original
print(numbers) # the order of the numbers in the list will be changed randomly each time you run the code
