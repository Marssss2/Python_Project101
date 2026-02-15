#inline statement is used to write the code in a single line. It is also known as ternary operator.
import random

score = random.randint(0, 100)

#if score >= 90:
#    print('A')
#else:
#    print('F')
    
grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F'
print(grade)
