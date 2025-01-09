from string import capwords

student_marks = {
    "Evelyne": 91,
    "Rozet": 78,
    "ElizaBeth": 90,
    "Peter": 89,

}
# for key, value in student_marks.items():
#     print("\nKey: " + key)
#     print("Value: " + value)

# if student_marks.get("Ryan"):
#     print("The student exists")
# else:
#     print("The student does not exist")

#This method is used to update the dictonary or change the values af an item
student_marks.update({"Selena": 78})
print(student_marks)
print("")

#This method removes the last item
student_marks.popitem()
print(student_marks)
print("")

#Removes a passed item into the dictionary
student_marks.pop("Rozet")
print(student_marks)
print("")

#The get method is used to check wwhether an item is present in the dictionary
print(student_marks.get("Peter"))
print("")

#The .keys method is used to loop through the keys
for key in student_marks.keys():
    print(key)
print("")

#The values method is used with the values
for value in student_marks.values():
    print(value)
print("")

#The items method if used to print, displays the dictionary as 2D tuple
items = student_marks.items()
print(items)
print("")
for key, value in student_marks.items():
    print(f"{key}: {value}")
