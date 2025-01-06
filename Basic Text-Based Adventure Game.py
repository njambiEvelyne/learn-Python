adventure = input("Enter your preferred mode for having fun: ")

if adventure == "Nature walk":
    print("You will have a guard to walk you through the wonderful land!")

elif adventure == "Go to the Zoo":

    parks = ["Nairobi National Park", "Nairobi Safari Walk"]
    print(parks)
    print("Choose from the above list of parks")
    zoo = input("Enter your preferred zoo: ")
    if zoo == "Nairobi National Park":
        print("Welcome to the park We will be waiting for you to arrive. ")
        stay = int(input("Enter the number of days you will be visiting the park to get the total expenses: "))

        if stay <2:
            print("The gross expenses sum to 20,000 per person")
        if stay ==2 or stay <4:
            print("The gross expense for a single person is 25,000")
        if stay ==4 or stay <7:
            print("The expense for a single person for a single day is 30,000")
        if stay ==7 or stay >7:
            print("The expense for a single person in a single day is 40,000")

    elif zoo == "Nairobi Safari Walk":
        print("We await your arrival to this amazing place!")
        total_number = int(input("How many are you: "))
        days_stay = int(input("Enter the number of days you will visit the park: "))
        if days_stay <2:
            fixed_cost = 10000
            gross_expense = (days_stay * total_number )* fixed_cost
            print(f"The total Expenses sum up to {gross_expense}")

        if days_stay ==2 or days_stay <5:
            fixed_cost = 20000
            gross_expense = (days_stay * total_number )* fixed_cost
            print(f"The total Expenses sum up to {gross_expense}")

        if days_stay ==5 or days_stay <7:
            fixed_cost = 30000
            gross_expense = (days_stay * total_number )* fixed_cost
            print(f"The total Expenses sum up to {gross_expense}")

        if days_stay >7:
            fixed_cost = 30000
            gross_expense = (days_stay * total_number )* fixed_cost
            print(f"The total Expenses sum up to {gross_expense}")


    else:
        print("Invalid park!")







