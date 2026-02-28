def Clean_split_email(email):
    cl_email = email.strip().lower()
    username, domain = cl_email.split('@')
    return {'username': username, 'domain': domain}

print(Clean_split_email('abemarasigAn@GMAIL.com'))

