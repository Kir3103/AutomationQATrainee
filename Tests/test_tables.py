import pytest

from Forms.RegistrationForm import RegistrationForm
from LogerUtils import Logger
from Pages.ElementsPage import ElementsPage
from Pages.TablesElementPage import TablesElementPage
from Pages.HomePage import HomePage
from ConfigTestData import ConfigTestData


@pytest.mark.parametrize("user_numb, expected", [(1, True), (2, True)])
class TestTables:

    def test_tables(self, get_webdriver, user_numb, expected):

        Logger.info('Go to the homepage')
        home_page_demoqa = HomePage()
        home_page_demoqa.is_page_open()
        assert home_page_demoqa, 'Demoqa main page is not open'

        Logger.info('Click on the "Elements button". '
                    'On the page that opens, click on "Web Tables" in the left-hand menu')
        home_page_demoqa.select_elements()
        elements_page = ElementsPage()
        elements_page.is_select_web_tables()
        element_tables = TablesElementPage()
        element_tables.is_page_open()
        assert element_tables, 'Form tables is not visible'

        Logger.info('Click on the "Add button"')
        element_tables.is_add_button_click()
        registration_from = RegistrationForm()
        registration_from.is_page_open()
        assert registration_from, 'Registration form is not opened'

        Logger.info('Enter User from the table and then click "Submit"')
        Logger.info('Get data from json file')
        expected_data_tables = ConfigTestData.get_values_from_users_data(user_numb)
        registration_from.fill_registration_form(expected_data_tables)
        registration_from.is_form_invisible()
        text_from_new_line = element_tables.is_new_line_in_tables()
        assert text_from_new_line == expected_data_tables, 'Values not added to tables'

        Logger.info('Press the "Delete" button on the User line')
        numbers_of_line_before_delete = element_tables.quant_line_in_table()
        element_tables.is_delete_button_click()
        numbers_of_line_after_delete = element_tables.quant_line_in_table()
        assert numbers_of_line_before_delete != numbers_of_line_after_delete, 'Quant line is equal'

        Logger.info('Checking the number of entries in the table and the text from the last row')
        text_from_new_line_after_delete = element_tables.is_previous_line_is_last()
        result = text_from_new_line_after_delete != expected_data_tables
        assert result == expected, 'Values are not deleted'
