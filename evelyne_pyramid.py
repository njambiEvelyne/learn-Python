def inverted_pyramid(name):
    n = len(name)

    # Iterate over the length of the name in reverse order
    for i in range(n, 0, -1):
        # Print spaces before the name
        spaces = ' ' * (n - i)
        # Print the name repeated 'i' times
        print(spaces + (name + ' ') * i)


# Example usage
name = input("Enter your name: ")
inverted_pyramid(name)
