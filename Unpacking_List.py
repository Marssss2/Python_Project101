lst = ['Maria', '29', 'Data Engineer', 'Manila']
name, age, profession, city = lst
print(f'name: {name}')
print(f'age: {age}')      
print(f'profession: {profession}')
print(f'city: {city}')


person = ['John', '30', 'Software Engineer', 'New York']

*details, city = person
name, age, profession = details
print(f'details: {details}')
print(f'city: {city}')

#rule match the value exactly the number of variables you want to unpack

details = ['John', '30', 'Software Engineer']
name, _, profession = details
print(f'name: {name}')
print(f'profession: {profession}')  
#Underscore is used as a placeholder for values we want to ignore during unpacking\
    
info = ['Alice', '25', 'Data Scientist', 'San Francisco', 'Python', 'Machine Learning', 'Deep Learning']
        
name, *_, skills = info
print(f'name: {name}')
print(f'skills: {skills}')  

# *_ is used to ignore multiple values during unpacking
# * is used to unpack the remaining values into a list, which can be useful when you want to ignore
# multiple values but still want to access the last value.