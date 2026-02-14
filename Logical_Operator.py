import random

print(3<5 and 5>2) # it will return true because both conditions are true.
print(3<5 or 5<2) # it will return true because at least one condition is true.
print(not(3<5)) # it will return false because 3 is less than 5, and the not operator negates the result.
print(not(5<2)) # it will return true because 5 is not less than 2, and the not operator negates the result.        



cpu_usage = random.randint(0, 100)
memory_usage = 95
if cpu_usage > 80 and memory_usage > 90:
    print("Warning: High resource usage!", cpu_usage)
else:
    print("Have a Nice Day")
    
    
    