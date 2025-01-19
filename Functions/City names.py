def city_country(city, country):
    return f"{city}, {country}"

while True:
    try:
        print("Enter the city and the country.....")
        print("Enter 'q' to quit at amy point.")

        city2 = input("Enter the city: ")
        country2 = input("Enter the country the city is found: ")

        if city2.lower() == "q":
            break
        if country2 == "q":
            break

        display = city_country(city2, country2)
        print(f"{city2.title()}, {country2.title()}")

    except ValueError:
        print("Invalid Input!")