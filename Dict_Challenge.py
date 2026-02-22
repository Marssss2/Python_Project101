user = {'id':1, 'name':'Abe', 'age':30, 'city':'Manila'} 

user_str = {
    k.upper(): v.lower()
    for k, v in user.items()
    if isinstance(v, str)
        
}

print(user_str)