class Employee:
    raise_amount = 1.50
    num_of_employees = 0

    def __init__(self, first, second, pay):
        self.first = first
        self.second = second
        self.email = first + '.' + second + '@gmail.com'
        self.pay = pay

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.second)

    def raise_pay(self):
        self.pay = self.pay * self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, second, pay = emp_str.split("-")
        return cls(first, second, pay)

    @staticmethod
    def is_weekDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}',{})".format(self.first, self.second, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)


class Developer(Employee):

    def __init__(self, first, second, pay, prog_lang):
        super().__init__(first, second, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, second, pay, employee=None):
        super().__init__(first, second, pay)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee

    def add_employee(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_employee(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def print_emp(self):
        for emp in self.employee:
            print(" -->", emp.fullname())


dev_1 = Developer('sunil', 'gulabani', 200000, 'java')
dev_2 = Developer('somnath', 'sharma', 40000, 'sql')

mgr_1 = Manager('Archana', 'singh', 500000, [dev_1])

print(mgr_1.email)

print(mgr_1.print_emp())

print(dev_1.fullname())
print(dev_1.email)

print(Employee.num_of_employees)
Employee.set_raise_amount(2.01)

emp_1 = Employee('vivek', 'mishra', 2000)
emp_2 = Employee('harsha', 'pandey', 50000)

emp_1.raise_amount = 2.0
emp_1.raise_pay()

# aarti-mishra-100000
input_data = 'aarti-mishra-100000'
new_employee = Employee.from_string(input_data)

print(new_employee.email)

print(Employee.num_of_employees)

print(emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)

print(emp_1.fullname())
Employee.fullname(emp_1)
print(Employee.fullname(emp_2))

import datetime

my_date = datetime.date(2018, 4, 2)
print(Employee.is_weekDay(my_date))
