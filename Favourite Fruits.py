favourite_fruit = ["Banana", "Guava", "Apples", "Pineapple"]

if "Banana" in favourite_fruit:
    print("\nBanana:")
    print("This fruit is sweet")
if "Guava" in favourite_fruit:
    print("\nGuava:")
    print("This is a very nutritious fruit")
if "Apples" in favourite_fruit:
    print("\nApples:")
    print("This fruit is so sweet")
if "Pineapple" in favourite_fruit:
    print("\nPineapples:")
    print("This fruit has a lot a sweet juice ")

else:
    print("Fruit not include in the list")

# This is a new program code.

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")