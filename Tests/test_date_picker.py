from DateUtils import DateUtils
from LogerUtils import Logger
from Models.DateModel import DateModel
from Pages.DatePickerPage import DatePickerPage
from Pages.HomePage import HomePage
from Pages.WidgetsPage import WidgetsPage
from ConfigTestData import ConfigTestData


class TestDatePicker:

    def test_date_picker(self, get_webdriver):

        Logger.info('Go to the homepage')
        home_page_demoqa = HomePage()
        home_page_demoqa.is_page_open()
        assert home_page_demoqa, 'Demoqa main page is not open'

        Logger.info('Click on the "Widgets" button. On the page that opens, click Date Picker '
                    'in the left-hand menu ')
        home_page_demoqa.select_widgets()
        widgets = WidgetsPage()
        widgets.is_select_date_picker()
        date_picker = DatePickerPage()
        date_picker.is_page_open()
        assert date_picker, 'Date Picker page is not opened'

        Logger.info('Check that the values in the "Select Date" and "Date And Time" fields match '
                    'the current date and time')
        assert date_picker.get_date_and_time_from_page() == \
               DateUtils.get_current_date_time_month(), 'Date, time and month are different'
        assert date_picker.get_date_from_select_date_element() == DateUtils.get_current_date(), \
            'Date and time are different'

        Logger.info('Using the "Date Picker box", set the date of the next February 29th '
                    'in the "Date Picker" field')
        date_picker.find_leap_date()
        date_after_input_value = date_picker.get_date_from_select_date_element_after_input()
        Logger.info('Get data from json file and put to DateModel')
        expected_date = DateModel(ConfigTestData.get_test_data_from_json('test_case_date_picker',
                                                                         'month')[1],
                                  ConfigTestData.get_test_data_from_json('test_case_date_picker',
                                                                         'date'),
                                  ConfigTestData.get_test_data_from_json('test_case_date_picker',
                                                                         'year'),
                                  None, None)
        assert date_after_input_value == expected_date, f'Expected date {expected_date} and ' \
                                                        f'date after select {date_after_input_value} ' \
                                                        f'in "Date Picker box" are different'
