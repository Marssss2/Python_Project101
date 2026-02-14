#Checkpoint that check conditional statements in Python.
#Conditional statements are used to perform different actions based on different conditions. The most common conditional statements in Python are if, elif, and else.
#double if statement is used to test multiple conditions. If the first condition is true, the block of code inside the first if statement will be executed. If the first condition is false, the second condition will be tested. If the second condition is true, the block of code inside the second if statement will be executed. If both conditions are false, the block of code inside the else statement will be executed.
#elif statement is used to test multiple conditions. If the first condition is true, the block of code inside the if statement will be executed. If the first condition is false, the second condition will be tested. If the second condition is true, the block of code inside the elif statement will be executed. If both conditions are false, the block of code inside the else statement will be executed.
# if statement is used to test a specific condition. If the condition is true, the block of code inside the if statement will be executed.
score = int(input("Enter your score: ")) 
submitted = input("Did you submit your assignment? (yes/no): ").lower()
if score >= 90 and submitted == "yes":
    print("You got an A!")
elif score >= 80:
    print("You got a B!")
elif score >= 70:
    print("You got a C!")
elif score >= 60 or submitted == "yes":
    print("You got a D!")
elif score <= 10:
    print("Parental guidance is advised.")
else:
    print("You got an F.")
    


 