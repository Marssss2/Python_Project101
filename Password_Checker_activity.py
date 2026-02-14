#Password Checker activity
ps = 'Password: '
password = input(ps)
if len(password) >= 8 and password != ' ' and not password.isdigit() and not password.isfloat() and len(password) <= 9:
    print("Welcome to the club!")
else:
    print('GO HOME')
    