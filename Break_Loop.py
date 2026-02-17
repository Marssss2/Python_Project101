#break it stops the loop immeadiately
#it Jumps out and Ends the loop right away

for i in (1,2,3):
    if i == 2: 
        break
    print (i)
    

names = ['Abe', 'Jelyn', 'Tonton', '', 'Cris']
for name in names:
    if name == '':
        print('Empty value Detected!')
        break
    print(f'Name = {name}')