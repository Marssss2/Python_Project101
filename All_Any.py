email = ''
phone = '09661700701'
username = 'admin'

print(any([email, phone, username])) #it will return true because phone and username are non-empty strings which are considered as true in boolean context.

print(all([email, phone, username])) #it will return false because email is empty string which is considered as false in boolean context.

print(isinstance(123, int)) # it will return true because 123 is an integer.
print(isinstance(True, str)) # it will return false because True is a boolean, not a string.