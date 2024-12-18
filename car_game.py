command = ""
while True:
    command = input("> ").lower()
    if command == "help":
        print('''
 start - for starting the car
 stop - for stopping the car
 quit - for quiting
        ''')
    elif command == "start":
        print("Car started...")
    elif command == "stop":
        print("The car has stopped.")
    elif command == "quit":
        break
    else:
        print("Sorry, I do not know this!")

