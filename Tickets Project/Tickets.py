feed = 0
while feed <3:
    try:
        age = int(input("Enter your age: "))
        feed += 1

        if age <3:
            print("Your ticket is free")
            break

        if age >=3 and age <=12:
            print("The ticket cost is $10.")
            break

        if age >12:
            print("The ticket cost is $15")
            break




    except ValueError:
        print("Invalid error. Enter integer value!")
    except Exception as a:
        print(f"Ran to unexpected error {a}")

