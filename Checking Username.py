current_users = ["evelyne", "peter", "elizabeth", "rose", "kim" "purity"]

new_users = input("Enter your preferred username: ").lower()
for user in current_users:
    if user in new_users:
        print("You will need to enter a new username")
        break
else:
    print("The username is available")
