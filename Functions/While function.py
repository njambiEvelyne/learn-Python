def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = first_name + ' ' + last_name
 return full_name.title()


#This is an infinite loop!
while True:
    print("\nPlease tell me your name...")
    print("(enter 'q' at any time to quit)")


    f_name = input("First name: ")
    l_name = input("Last name: ")

    if f_name == 'q':
        break

    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")