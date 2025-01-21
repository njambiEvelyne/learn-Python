#It is called when an object is about to get destroyed
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        try:
            self.file = open(filename, 'r')  # Open the file for reading

        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            self.file = None

    def read_data(self):
        if self.file:
            return self.file.read()
        return "No file to read."

    def __del__(self):
        if self.file:
            self.file.close()
            print(f"File '{self.filename}' closed.")


file_obj = FileHandler('car_game.py')
print(file_obj.read_data())