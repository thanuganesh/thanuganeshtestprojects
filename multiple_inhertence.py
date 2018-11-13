""" Going to learn about multiple inhertence"""
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_language):
        super().__init__(first, last, pay) #for multiple inhertence should clean and maintainable the super key word
        #first last pay take care by employee class prog_lanuage take care by prog_lanuage
        #Employee.__init__(self, first, last, pay) #for single inhertence should clean and maintainable then normai class inhertiance    
        self.prog_language = prog_language # this like normal class declartion
    def fullname(self):
        return "{} {} ;;;;".format(self.first, self.last)

class Manager(Employee):

    def __init__(self, first, last , pay, employees=None):
        super().__init__(first, last , pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_emps(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
       for emp in self.employees:
            print("---->", emp.fullname())






#dev_1 = Employee('thanu', 'ganesh', '900000')
#dev_2 = Employee('vino', 'ganesh', '30000000')

dev_1 = Developer('thanu', 'ganesh', 900000, "python")
dev_2 = Developer('vino', 'ganesh', 300000, "java")

man_1 = Manager('thanu', 'ganesh', 900000, [dev_1])


man_1.add_emps(dev_2)

man_1.rem_emp(dev_1)
print(man_1.email)
print(man_1.print_emps())
#print(dev_2.prog_language)
print(isinstance(man_1, Developer))
print(issubclass(Developer, Employee))

#print(help(dev_1))
#print(dev_1.pay)

#dev_1.apply_raise()

#print(dev_1.pay)
