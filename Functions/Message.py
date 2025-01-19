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
