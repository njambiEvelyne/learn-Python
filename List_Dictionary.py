#Inclusion of multiple dictionaries in a single list
pizza = [
    {"toppings": "mushroom, extra cheese"},
    {"feel": "crust, thick"}
]
print(pizza[0])
for toppings in pizza:
    print(toppings)


#Using the enumerate function
hobby = ["coding", "reading", "watching"]
for place, loved_hobby in enumerate(hobby, start=1):
    print(f"{place}. {loved_hobby}")

print("")


#Associating of multiple lists in a single dictionary
opted_languages = {
    "Jen":["python", "ruby"],
    "Sarah":["c"],
    "Edward": ["ruby", "go"],
    "phil": ["python", "haskell"]
}
#The enumeration function is used to display even the index
print("The output below is for people and their languages")
for  name, languages in enumerate(opted_languages.items(), start=1):
    print(f"{name}. {languages}")
print("")

for name, languages in opted_languages.items():
    print("")
    print(f"{name}'s favourite languages are:\n {languages}")
