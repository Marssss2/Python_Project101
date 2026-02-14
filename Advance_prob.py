mess = '968-Maria, ( D@t@ Engineer ) ;; 27y  '

print(mess.replace('@','a').replace('968','Name:').replace('(','Role:').replace('-','').lstrip('Data Engineer').replace(')','').replace(';;','Age:').replace('y',' years old').strip().replace(',',''))