"""This area will learn about context managers"""
from contextlib import contextmanager
import os

f = open("sample.txt", "w")

f.write("I am Your Thanuuuuu!!!!!!!!!!!!!!!!!")

f.close()

# Context managers allows properly manages the resoucers like Db, ssh , fileoperations and so on

# "With" - no needs to clone manually 

"""
class Open_File():

    def __init__(self , destination):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, traceback):
        pass
"""

class Open_File():

    def __init__(self , filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode) #self.file is new instance variable
        
        return self.file #Here return the object what we are currently working with context manager
        #enter () method return the setup object to the with inside with f is eneterd return object

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

with Open_File("sample.txt", "w") as f:
    
    f.write("thanu testing!!!!")



print(f.closed) #wen exists run 



@contextmanager
def open_File(file_name,mode):
    try:
        f =open(file_name, mode) #equalent to enter method
        yield f
    finally:
        f.close() #equalent to exit method

with open_File("sample.txt","a") as f:

    f.write("\nthanu back to form!!!!!!!!!!!!!!!")



#cwd =os.getcwd()
#os.chdir('thanuganeshtestprojects')
#print(os.listdir())
#os.chdir(cwd)




@contextmanager
def change_dir(desination):
    try:
        cwd = os.getcwd()
        os.chdir(desination)
        yield  #not working with any variable yield f becaz we working with the f object
    finally:
        os.chdir(cwd)


with change_dir('thanuganeshtestprojects'):
    print(os.listdir())

#we can reuse the context manager over and over mangages


