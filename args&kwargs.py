def total(*args):
    print(sum(args))
       
total(1,2,3,4,5)

def create_user(**kwargs):
    print(kwargs)

create_user(name='Angelo', age=25, country='Philippines')