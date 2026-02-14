phone = '+48-176-12345'
print(phone.startswith('+49'))  # False

email = 'abemarasigan134@gmail.com'
print(email.endswith('@gmail.com'))  # True 

file = 'data_backup.csv'
print(file.endswith('.csv'))  # True

email = 'abemarasigan134@gmail.com'
print('@' in email)

url = 'https://www.example.com'
print(url.startswith('https://'))  # True


phone1 = '+48-176-12345'
phone2 = '49-176-12345'

print(phone1[phone1.find('-')+1:]) #176-12345
print(phone2[3:])  # '176-12345' it will give you the substring starting from index 3 to the end of the string, which is '176-12345'

print(phone1.find('-')) #3 it will give you the index of the first occurrence of the hyphen in the phone number


