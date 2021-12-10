# Program to Create, delete the file

import os

#create file "abc.txt"
file=open("C:\\Users\\user\\PycharmProjects\\pythonBasics\\PythonBasicPrograms\\ProjectFiles\\abc.txt","x")

file.close() # close file

# delete file "abc.txt"
os.remove("C:\\Users\\user\\PycharmProjects\\pythonBasics\\PythonBasicPrograms\\ProjectFiles\\abc.txt")


