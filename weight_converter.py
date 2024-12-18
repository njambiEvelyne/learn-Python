Weight = input("Enter your weight in(pounds or kg)").lower()

match Weight:
    case "kg":
        kg = int(input("Enter your weight(kg): "))
        pound_weight = kg / 0.4
        print(f"Your weight in pounds is {pound_weight} pounds")
    case "pounds":
        pounds = int(input("Enter your weight(pounds): "))
        kg_weight = pounds * 0.4
        print(f"Your weight in kg is {kg_weight} kilograms")
    case _:
        print("Invalid weight conversion units")




