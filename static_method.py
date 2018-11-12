""" Going to learn about staic method 
    Regular methaod takes self as first arugument
    class method takes takes cls as a first argument
    static method nothing needs but there some logical connectivity with class"""

class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_emps +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amt):
        cls.raise_amt = amt

    @classmethod
    def string_split(cls, new_str):
        first , last , pay = new_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def check_type(obj):
        if isinstance(obj, str):
            return True
        return False

emp_1 = Employee('thanu','ganesh',50000)
emp_2 = Employee('kiru', 'sunt' , 60000)

#class method are called anthor constructer for the class
#emp_1.set_raise_amt(1.06)
#Employee.set_raise_amt(1.05)

#print(Employee.raise_amt)
#print(emp_1.raise_amt)
#print(emp_2.raise_amt)

new_string = "thanu-vinay-090000"

#first , last , pay = new_string.split("-")

#new_emp1 = Employee(first, last , pay)

#new_emp1 = Employee.string_split(new_string)
print(Employee.check_type(emp_1.first))
#print(new_emp1.pay)

    
