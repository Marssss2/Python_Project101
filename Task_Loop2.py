emails = [
    'data@gmail.com',
    'marasigan@gmail.com',
    'baraa@gmail.com',
    'DORP TABLE USER;',
    'abemarasigan@gmail.com'
    ]

for email in emails:
    if ';' in email:
        print(f'SQL INJECTION: HACKER ATTACK')
        break
    print(f'Processing Email:{email}')