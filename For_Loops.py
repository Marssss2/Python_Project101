#for loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects. It allows you to execute a block of code repeatedly for each item in the sequence.
#for i in range(5):
#    print(i)   

from tracemalloc import start, stop

from click import group
from matplotlib.pyplot import step
#start is used to start the for loop and stop is used to end the for loop. The code inside the for loop will be executed for each item in the sequence.
#stop is used to stop the for loop. The code inside the for loop will not be executed after the stop statement is reached.
#step is used to specify the step size for the for loop. The default step size is 1, which means that the for loop will iterate over every item in the sequence. If you specify a step size of 2, for example, the for loop will iterate over every other item in the sequence.


for i in range(1,10,2):
    print(f"Round {i}")
    
items = ['apple', 'banana', 'cherry']
for item in items:
    print(f"Item: {item}")
    

grocery = [10, 20, 30, 40, 50, 'Milk']
for item in grocery:
    print(f"Item: {item}")
    
    