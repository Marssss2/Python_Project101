email = input("Enter your email: ")
password = input("Enter your password: ")

correct_email = "admin@gmail.com"
correct_password = "Admin123"

if email == correct_email and password == correct_password:
    print("Login successful!")
elif password == "":
    print("Password cannot be empty.")
elif len(password) < 8:
    print("Password must be at least 8 characters long.")
elif password.upper() == password:
    print("Password must contain at least one lowercase letter.")
elif password.lower() == password:
    print("Password must contain at least one uppercase letter.")
elif password.isalpha():
    print("Password must contain at least one number.")
elif password.isnumeric():
    print("Password must contain at least one letter.")
elif password.isspace():
    print("Password cannot contain only spaces.")
elif password == email:
    print("Password cannot be the same as the email address.")
elif password[0].isdigit():
    print("Password cannot start with a number.")
elif password[-1].isdigit():
    print("Password cannot end with a number.")

else:
    print("Email or password is incorrect!")
