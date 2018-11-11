" Thais function helps to learn property decortor"""


class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.new = "thanuuu"
	#self.email = first + "." + last + '@emil.com'
   
    @property
    def email(self):
        """This function helps to potrait how we can access method as Atrribute in python using property class"""
        return '{}.{}@email.com'.format(self.new, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first,last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print ('object deleted successfully')

emp_1 = Employee('thanu', 'ganesh')

emp_1.fullname = "corey schefer"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname



print(emp_1.fullname)
