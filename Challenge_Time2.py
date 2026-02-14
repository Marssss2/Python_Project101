email = input("Enter your email: ")

if email == "":
    print("Email address cannot be empty.")

elif "@" not in email or "." not in email:
    print("Invalid email address.")

elif email.count("@") != 1:
    print("Invalid email address.")

elif not (email.endswith(".com") or 
          email.endswith(".net") or 
          email.endswith(".org")):
    print("Invalid email address.")

elif len(email) > 254:
    print("Invalid email address.")

else:
    print("Valid email address.")
