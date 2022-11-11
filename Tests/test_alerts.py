from AlertUtils import AlertUtils
from LogerUtils import Logger
from Pages.AlertPage import AlertPage
from Pages.AlertsFrameWindowsPage import AlertsFrameWindowPage
from Pages.HomePage import HomePage
from ConfigTestData import ConfigTestData
from StringUtils import StringUtils


class TestAlerts:

    def test_alerts(self, get_webdriver):

        Logger.info('Go to the homepage')
        home_page_demoqa = HomePage()
        home_page_demoqa.is_page_open()
        assert home_page_demoqa, 'Demoqa main page is not open'

        Logger.info('Click on the button "Alerts, Frame & Windows button. '
                    'On the page that opens, click on Alerts in the left-hand menu"')
        home_page_demoqa.select_alerts_frames_windows()
        alerts_frame_windows = AlertsFrameWindowPage()
        alerts_frame_windows.is_select_button_alert()
        alerts_frame_windows.is_page_open()
        assert alerts_frame_windows, 'Alert form is not open'

        Logger.info('Click "Click Button to see alert"')
        alert = AlertPage()
        alert.is_alert_form_button_see_click()
        alert_utils = AlertUtils()
        alert_utils.is_alert_visible()
        assert ConfigTestData.get_test_data_from_json('test_case_alert', 'message_from_alert')[0] \
               in alert_utils.get_text_from_alert(), '"You clicked a button" is not visible'

        Logger.info('Press the "OK" button')
        alert_utils.accept_alert()
        alert.check_alert_closed()
        assert alerts_frame_windows, 'Alert closed'

        Logger.info('Click "On button click, confirm box will appear"')
        alert.is_alert_form_button_confirm_click()
        alert_utils.is_alert_visible()
        assert ConfigTestData.get_test_data_from_json('test_case_alert', 'message_from_alert')[1] \
               in alert_utils.get_text_from_alert(), '"Do you confirm action?" is not visible'

        Logger.info('Press the "OK" button')
        alert_utils.accept_alert()
        assert ConfigTestData.get_test_data_from_json('test_case_alert',
                                                      'message_from_page_near_button') \
               in alert.get_text_from_alert_confirm(), '"You selected Ok" is not visible'

        Logger.info('Click "On button click, prompt box will appear"')
        alert.is_alert_form_button_box_click()
        alert_utils.is_alert_visible()
        assert ConfigTestData.get_test_data_from_json('test_case_alert', 'message_from_alert')[2] \
               in alert_utils.get_text_from_alert(), '"Please enter your name" is not visible'

        Logger.info('Enter random generated text and then press the "OK" button')
        random_text = StringUtils.generate_random_string()
        alert_utils.send_text_to_alert(random_text)
        text_from_alert_box = alert.get_text_from_alert_form_button_box()
        assert random_text in text_from_alert_box, 'Entered text do not equals the text on the page'
