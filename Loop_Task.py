
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    answer = input("Do you agree? (yes/no): ").strip().lower()
    
    if answer == "yes":
        print("Thank you for agreeing!")
        break  # exit loop if yes
    else:
        attempts += 1
        if attempts < max_attempts:
            print(f"Incorrect response. You have {max_attempts - attempts} attempts left.")
        else:
            print("You are out. You are out.")
