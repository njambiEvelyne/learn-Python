name = input("Enter your name:")
if len(name) <3:
    print("The name must be at least 3 characters")
elif len(name) >50:
    print("Name can be maximum of 50 characters")
else:
    print("Name looks good!")
