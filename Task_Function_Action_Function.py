def write_log(message):
    with open(r"D:\Python\app.log", 'a') as f:
        f.write(message + '\n')

#write_log('App Started')
write_log('User log in!')
