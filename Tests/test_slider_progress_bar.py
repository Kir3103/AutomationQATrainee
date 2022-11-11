from LogerUtils import Logger
from Pages.HomePage import HomePage
from Pages.ProgressBarPage import ProgressBarPage
from Pages.SliderPage import SliderPage
from Pages.WidgetsPage import WidgetsPage


class TestSliderProgressBar:

    def test_slider_progress_bar(self, get_webdriver):

        Logger.info('Go to the homepage')
        home_page_demoqa = HomePage()
        home_page_demoqa.is_page_open()
        assert home_page_demoqa, 'Demoqa main page is not open'

        Logger.info('Click on the "Widgets" button. Select "Slider" from the left-hand menu')
        home_page_demoqa.select_widgets()
        widgets = WidgetsPage()
        widgets.is_select_slider_button()
        slider = SliderPage()
        slider.is_page_open()
        assert slider, 'Slider form is not opened'

        Logger.info('Set the slider to the correct randomly generated value')
        slider_value = slider.get_random_number()
        slider.is_slider_moved(slider_value)
        new_slider_value = slider.get_value_slider()
        assert new_slider_value == slider_value, 'Values are not equal'

        Logger.info('Select "Progress Bar" from the left-hand menu')
        slider.is_select_progress_bar()
        progress_bar = ProgressBarPage()
        progress_bar.is_page_open()
        assert progress_bar, 'Progress Bar form is not opened'

        Logger.info('Click on the "Start" button')
        progress_bar.is_start_button_click()
        Logger.info('Press the "Stop" button when the download bar shows a value equal to the '
                    'age of the engineer carrying out the task')
        progress_bar.is_stop_button_click()
        progress_bar.get_value_progress_bar()
        assert progress_bar.compare_values_progress_bar(), 'Progress Bar value value is not in ' \
                                                           'the range of the correct age'
