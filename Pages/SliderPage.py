from Elements.BaseElement import BaseElements
from Elements.Slider import Slider
from Pages.BasePage import BasePage
from RandomNumberUtils import RandomNumberUtils
from ConfigTestData import ConfigTestData


class SliderPage(BasePage):
    form_slider = BaseElements('//*[@id="sliderContainer"]', 'Slider')
    locator_move_slider = '//*[@id="sliderContainer"]//input[contains(@class,"slider")]'
    locator_value_slider = '//*[@id="sliderValue"]'
    locator_select_progress_bar = '//*[contains(@class,"collapse")]//span[contains(text(),"{0}")]'.\
        format(ConfigTestData.get_test_data_from_json('test_case_slider_progress', 'button')[1])

    def __init__(self):
        self.move_slider = Slider(SliderPage.locator_move_slider, 'Move Slider')
        self.value_slider = Slider(SliderPage.locator_value_slider, 'Slider value')
        self.select_progress_bar = BaseElements(SliderPage.locator_select_progress_bar,
                                                'Progress Bar')
        super().__init__(unique_elem=SliderPage.form_slider, name_log='Slider')

    def get_random_number(self):
        example_max_value = 100
        example_min_value = 0
        slider_max = float(self.move_slider.get_value_from_elem("max") or example_max_value)
        slider_min = float(self.move_slider.get_value_from_elem("min") or example_min_value)
        return RandomNumberUtils.random_number_utils(slider_min, slider_max)

    def is_slider_moved(self, value):
        return self.move_slider.move_slider_on_value(value)

    def get_value_slider(self):
        return int(self.value_slider.get_value_from_elem("value"))

    def is_select_progress_bar(self):
        return self.select_progress_bar.click_script()
