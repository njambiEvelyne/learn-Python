favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

name = input("Enter your name: ").lower()
if name in favorite_languages:
 print(f"{name.title()}: You have taken the poll and your favourite language is {favorite_languages[name]}.")

else:
 print(f"Sorry {name.title()}. You have to do a poll to determine your favourite language!")

my_list = ["Hello", "Hii", "You are good!"]
print("A list printed using the enumerate function")
for i , greeting in enumerate(my_list, start= 1):
    print(f"{i}. {greeting}")
print("")

my_tuple = (1,2,3,5,8,4,89)
print("A Tuple that is printed using the enumerate function")
for i ,tuple in enumerate(my_tuple, start=1):
    print(f"{i}. {tuple}")

