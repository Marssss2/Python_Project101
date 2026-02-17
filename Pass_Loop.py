names = ['Abe', 'Jelyn', 'Tonton', '', 'Cris']
for name in names:
    if name == '':
        pass
        name = name.replace('', 'NULL')   
    print(f'Name = {name}')