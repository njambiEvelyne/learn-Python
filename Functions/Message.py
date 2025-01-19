def display_message(title,lesson_learnt):
    """To display the user's concept of reading."""

    return f"I am reading a book called {title.title()}.\n I have learnt the following: {lesson_learnt}"

print(display_message("The untamed", '''
1. Be a courageous woman in all your pursuits.
2. A woman has a big potential which gets suppressed by the society.
3. I do believe in my abilities.
4. I must achieve all it is that I want to in life.
5. I need God in all that I do.  
6. A prayer to ensure I stay aligned with the will if God.
'''))

def book_title (lesson = "", title = "Untamed"):
    return f"The title is {title}"

print(book_title("""
1. Hello
"""))

book = book_title()
print(book)

def build_person(first_name, last_name):
    person = {"First name":first_name, "Second Name": {last_name}}
    return person

print(build_person("Evelyne", "Njambi"))

