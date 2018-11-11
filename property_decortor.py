" Thais function helps to learn property decortor"""


class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
	self.email = first + "." + last + '@emil.com'
   
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('thanu', 'ganesh')


print(emp_1.first)
print(emp_1.email)
print(emt_1.fullname())
