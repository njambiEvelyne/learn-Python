def greet_user(names):
    """Print a simple greeting to each of the users"""
    for name in names:
        msg = "Hello " + name
        print(msg)

user_names = ["Evelyne", "Rose", "Nelly"]
print(greet_user(user_names))
