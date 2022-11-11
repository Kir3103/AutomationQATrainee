from DateUtils import DateUtils
from Elements.BaseElement import BaseElements
from Elements.DropDownList import DropDownList
from LeapYearUtils import LeapYearUtils
from LogerUtils import Logger
from Models.DateModel import DateModel
from Pages.BasePage import BasePage
from ConfigTestData import ConfigTestData


class DatePickerPage(BasePage):
    form_date_picker = BaseElements('//*[@id="datePickerContainer"]', 'Form Date Picker')
    locator_date_and_time_from_page = '//*[@id="dateAndTimePickerInput"]'
    locator_date_from_select_date_element = '//*[@id="datePickerMonthYearInput"]'
    locator_select_month = '//*[contains(@class,"month-dropdown")]' \
                           '//select[contains(@class,"month-select")]'
    locator_select_year = '//*[contains(@class,"year-dropdown")]' \
                          '//select[contains(@class,"year-select")]'
    locator_select_date = '//*[@class="react-datepicker__month"]' \
                          '//div[contains(@aria-label,"{0} {1}")]'.\
        format(ConfigTestData.get_test_data_from_json('test_case_date_picker', 'month')[0],
               ConfigTestData.get_test_data_from_json('test_case_date_picker', 'date'))

    def __init__(self):
        self.date_and_time_from_page = BaseElements(DatePickerPage.locator_date_and_time_from_page,
                                                    'Date and Time from Page')
        self.date_from_select_date_element = BaseElements(DatePickerPage.
                                                          locator_date_from_select_date_element,
                                                          'Date from select date element')
        self.select_month = DropDownList(DatePickerPage.locator_select_month, 'Select Month')
        self.select_year = DropDownList(DatePickerPage.locator_select_year, 'Select Year')
        self.select_date = BaseElements(DatePickerPage.locator_select_date, 'Select date')
        super().__init__(unique_elem=DatePickerPage.form_date_picker, name_log='Date Picker')

    def get_date_and_time_from_page(self):
        Logger.info('Get month, day, year, hours and minutes from module DatePickerPage and '
                    'convert to compare view')
        list_with_date = (self.date_and_time_from_page.get_value_from_elem('value')).split()
        month = list_with_date[0]
        day = list_with_date[1].replace(',', '')
        year = list_with_date[2]
        hours_minutes = list_with_date[3]
        pm_or_am = list_with_date[4]
        Logger.info('Get all values from DatePickerPage after convert to DateModel')
        current_value_to_model = DateModel(month, day, year, hours_minutes, pm_or_am)
        return current_value_to_model

    def get_date_from_select_date_element(self):
        Logger.info('Get month, day and year from "Select date" element')
        date_from_element = self.date_from_select_date_element.get_value_from_elem('value')
        return date_from_element

    def find_leap_date(self):
        year = int(DateUtils.get_current_date().replace('/', ' ').split()[2])
        Logger.info(f'Check if the current year {year} is leap. '
                    f'If Yes, then find need date in current year')
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            self.date_from_select_date_element.click_regular()

            self.select_month.select_item_by_visible_text(ConfigTestData.
                                                          get_test_data_from_json
                                                          ('test_case_date_picker', 'month')[0])
            return self.select_date.click_regular()
        else:
            Logger.info(f'Compare the sum of the days {LeapYearUtils.get_sum_days()} in the '
                        f'current year and the average value of the days in the year')
            if LeapYearUtils.get_sum_days() >= 182:
                self.date_from_select_date_element.click_regular()
                for i in range(0, 4):
                    if (year + i) % 400 == 0 or (year + i) % 4 == 0 and (year + i) % 100 != 0:
                        self.select_month.select_item_by_visible_text(ConfigTestData.
                                                                      get_test_data_from_json
                                                                      ('test_case_date_picker',
                                                                       'month')[0])
                        self.select_year.select_item_by_value(f'{year + i}')
                        return self.select_date.click_regular()
                    else:
                        continue
            else:
                self.date_from_select_date_element.click_regular()
                for i in range(0, 4):
                    if (year - i) % 400 == 0 or (year - i) % 4 == 0 and (year - i) % 100 != 0:
                        self.select_month.select_item_by_visible_text(ConfigTestData.
                                                                      get_test_data_from_json
                                                                      ('test_case_date_picker',
                                                                       'month')[0])
                        self.select_year.select_item_by_value(f'{year - i}')
                        return self.select_date.click_regular()
                    else:
                        continue

    def get_date_from_select_date_element_after_input(self):
        Logger.info('Get month, day and year from "Select date" element after select date')
        date_from_element = self.date_from_select_date_element.get_value_from_elem('value')
        list_date_to_compare = date_from_element.replace('/', ' ').split()
        month = list_date_to_compare[0]
        day = list_date_to_compare[1]
        year = list_date_to_compare[2]
        current_date = DateModel(month, day, year, None, None)
        return current_date
