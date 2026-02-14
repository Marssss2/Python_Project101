
#Check is a user name is not empty and if the user is 18 years old or older. If both conditions are true, print "Welcome to the club!", otherwise print "Sorry, you are not allowed to enter the club." 
#Python Challenge 101: User Authentication
user = input("Username: ")
age = input("Age: ")

print(user)
if user != ' ' and int(age) >= 18:    
    print("Welcome to the club!") 
else:   
    print("Sorry, you are not allowed to enter the club.") 