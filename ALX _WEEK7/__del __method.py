#It is called when an object is about to get destroyed
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')#Open the file for reading

    def read_data(self):
        return self.file.read()

    def __del__(self):
        self.file.close()#close the file when the object is destroyed

file_obj = FileHandler('sample.txt')
print(file_obj.read_data())
