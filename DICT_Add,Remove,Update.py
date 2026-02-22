user = {'id':1, 'username':'john_doe', 'email':'john@example.com'}

user['age'] = 30 #it means that we are adding a new key 'age' with value 30 to the dictionary
print(user) #it means that the dictionary now contains the new key 'age' with its value 30

user.update({'age': 35, 'city': 'New York'}) #it means that we are updating the dictionary with new key-value pairs
print(user) #it means that the dictionary now contains the updated key-value pairs for 'age' and 'city'