# Step 1: Create a dictionary with student names and their scores
students_scores = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "Diana": 68,
    "Ethan": 78
}

# Step 2: Print the dictionary
print("Initial dictionary:", students_scores)

# Step 3: Add a new student and their score
students_scores["Fiona"] = 88
print("After adding a new student:", students_scores)

# Step 4: Update the score of an existing student
students_scores["Bob"] = 80
print("After updating Bob's score:", students_scores)

# Step 5: Remove a student from the dictionary
del students_scores["Diana"]
print("After removing Diana:", students_scores)

# Step 6: Print names of all students who scored above 75
print("Students who scored above 75:")
for student, score in students_scores.items():
    if score > 75:
        print(student)
