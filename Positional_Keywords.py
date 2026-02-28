def clean_name(first_name,last_name,Country):

    Country = Country.strip().upper()
    first = first_name.strip().upper()
    last = last_name.strip().upper()
    fullname = first + ' ' + last
    print('Cleaned name: '+fullname)
    print('Country: '+ Country)
    
    
clean_name('Angelo  ',' MArasigan','   Philippines  ')#POSITIONAL ARGUMENTS

clean_name(last_name=' MArasigan',first_name='Angelo  ',Country='Dubai') #KEYWORD ARGUMENTS   

clean_name(' mARASIGAN', last_name ='Marasigan ', Country='   Philippines  ') #MIXED ARGUMENTS