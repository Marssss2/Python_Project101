user = {'Id':1, 'username:':'john_doe:', 'email:':'john@example.com'}

#Looping
for u in user:
    print(u,user[u]) #it means that it will print the keys of the dictionary

for key, value in user.items():
    print(key, value) #it means that it will print the keys and values of the dictionary    