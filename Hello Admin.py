user_names = ["admin", "Evelyne", "Peter","Eliza","Rose"]

for user_name in user_names:
    if user_name == "admin":
        print("Hello admin, would you like to see a status report?\n")
    else:
        print(f"Hello {user_name}, thankyou for logging in again.\n")

