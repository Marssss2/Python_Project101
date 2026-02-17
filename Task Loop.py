days = [
    'Mon',
    'Tue',
    'Wed',
    'Thur',
    'Fri',
    'Sat',
    'Sun'
    ]
for day in days:
    if day in ['Sat', 'Sun']:
        continue
    print(f'Workdays:{day}')
