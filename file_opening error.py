def open_file():
    file_name = input("Enter the file to be opened: ")

    try:
        with open(file_name, "r") as file:
            content = file.read()
            print('File content:')
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


open_file()