from Elements.BaseElement import BaseElements
from Elements.Button import Button
from Elements.TextField import TextField
from Models.EmployeeModel import EmployeeModel
from Pages.BasePage import BasePage


class RegistrationForm(BasePage):
    opened_registration_form = BaseElements('//*[@class="modal-body"]', 'Registration form')
    locator_first_name = '//*[@id="firstName"]'
    locator_last_name = '//*[@id="lastName"]'
    locator_email = '//*[@id="userEmail"]'
    locator_age = '//*[@id="age"]'
    locator_salary = '//*[@id="salary"]'
    locator_department = '//*[@id="department"]'
    submit_button = Button('//*[@id="submit"]', 'Submit')
    closed_registration_form = BaseElements('//*[@class="modal-body"]', 'Registration form')

    def __init__(self):
        self.first_name = TextField(RegistrationForm.locator_first_name, 'First Name')
        self.last_name = TextField(RegistrationForm.locator_last_name, 'Last Name')
        self.email = TextField(RegistrationForm.locator_email, 'Email')
        self.age = TextField(RegistrationForm.locator_age, 'Age')
        self.salary = TextField(RegistrationForm.locator_salary, 'Salary')
        self.department = TextField(RegistrationForm.locator_department, 'Department')
        super().__init__(unique_elem=RegistrationForm.opened_registration_form,
                         name_log='Registration form')

    def fill_registration_form(self, user_form: EmployeeModel):
        self.first_name.send_keys(user_form.first_name)
        self.last_name.send_keys(user_form.last_name)
        self.email.send_keys(user_form.email)
        self.age.send_keys(user_form.age)
        self.salary.send_keys(user_form.salary)
        self.department.send_keys(user_form.department)
        return self.submit_button.click_script()

    def is_form_invisible(self):
        return self.closed_registration_form.invisibility_element()
