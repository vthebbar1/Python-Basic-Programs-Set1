# Program to open , append and close the file

file=open("C:\\Users\\user\\PycharmProjects\\pythonBasics\\PythonBasicPrograms\\ProjectFiles\\DataFile.txt","a")
file.write("Appended line\n")
file.close()

# Read the file
file=open("C:\\Users\\user\\PycharmProjects\\pythonBasics\\PythonBasicPrograms\\ProjectFiles\\DataFile.txt","r")
print(file.read())
file.close()