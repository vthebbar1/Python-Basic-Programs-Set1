# Program to read the file.

file=open("C:\\Users\\user\\PycharmProjects\\pythonBasics\\PythonBasicPrograms\\ProjectFiles\\DataFile.txt","r")

# Read the entire file
a=file.read()
print(a)
file.close()

print("*******************")
file=open("C:\\Users\\user\\PycharmProjects\\pythonBasics\\PythonBasicPrograms\\ProjectFiles\\DataFile.txt","r")
# Read specified number of characters from a file
b=file.read(4)
print(b)
file.close()

print("*******************")
file=open("C:\\Users\\user\\PycharmProjects\\pythonBasics\\PythonBasicPrograms\\ProjectFiles\\DataFile.txt","r")
# Read first line of a file
c=file.readline()
print(c)
file.close()


print("*******************")
file=open("C:\\Users\\user\\PycharmProjects\\pythonBasics\\PythonBasicPrograms\\ProjectFiles\\DataFile.txt","r")
# Read the entire file as a list
d=file.readlines()
print(d)