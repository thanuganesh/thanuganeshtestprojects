


class Developer():

    def __call__(self, name):
        return name


class Employee(Developer):

    no_of_obj = 1
    
    def __call__(self, name): 
        print(super().__call__(name))

obj = Employee()

obj("thanu")




#########################class EXceptions####################################

class Thanuownexception(Exception):
    pass


class Program():
    #pass
    def __bool__(self):
        return True
    def __len__(self):
        return self    

    __len__ = __bool__


obj = Program()

print(len(obj))
