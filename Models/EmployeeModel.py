class EmployeeModel:

    def __init__(self, first_name, last_name, email, age, salary, department):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__age = age
        self.__salary = salary
        self.__department = department

    def __eq__(self, other):
        return (self.__first_name, self.__last_name, self.__email, self.__age, self.__salary,
                self.__department) == (other.__first_name, other.__last_name, other.__email,
                                       other.__age, other.__salary, other.__department)

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, another_first_name):
        self.__first_name = another_first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, another_last_name):
        self.__last_name = another_last_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, another_email):
        self.__email = another_email

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, another_age):
        self.__age = another_age

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, another_salary):
        self.__salary = another_salary

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, another_department):
        self.__department = another_department
