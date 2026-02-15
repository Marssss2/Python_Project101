country = input('Enter a country name: ')
if country == 'Philippines':
    print('PH')
elif country == 'United States':
    print('US')
elif country == 'Japan':
    print('JP')
elif country == 'India':
    print('IN')
elif country == 'Australia':
    print('AU')
elif country == 'United Kingdom':
    print('UK')
else:
    print('Unknown Country')

# The match statement is a new feature in Python 3.10 that allows you to write more concise and readable code when you have multiple conditions to check. It is similar to the switch statement in other programming languages. The match statement uses pattern matching to compare

match country:
    case 'Philippines'|'Peso':
        print('PH')
    case 'United States':
        print('US')
    case 'Japan':
        print('JP')
    case 'India':
        print('IN')
    case 'Australia':
        print('AU')
    case 'United Kingdom':
        print('UK')
    case _:
        print('Unknown Country')
 