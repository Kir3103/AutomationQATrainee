from Browser.WebDriver import WebDriver
from HandlesUtils import HandlesUtils
from LogerUtils import Logger
from Pages.AlertsFrameWindowsPage import AlertsFrameWindowPage
from Pages.HandlesPage import HandlesPage
from Pages.HomePage import HomePage
from Pages.LinksPage import LinksPage
from Pages.SamplePage import SamplePage
from ConfigTestData import ConfigTestData


class TestHandles:

    def test_handles(self, get_webdriver):

        Logger.info('Go to the homepage')
        home_page_demoqa = HomePage()
        home_page_demoqa.is_page_open()
        assert home_page_demoqa, 'Demoqa main page is not open'

        Logger.info('Click on the "Alerts, Frame & Windows button". '
                    'On the page that opens, click on Browser Windows in the left-hand menu')
        home_page_demoqa.select_alerts_frames_windows()
        alerts_frame_windows = AlertsFrameWindowPage()
        alerts_frame_windows.is_select_button_handles()
        handles = HandlesPage()
        handles.is_page_open()
        assert handles, 'Form Browser Windows is not open'

        handles_utils = HandlesUtils()
        demoqa_handle = handles_utils.get_current_handle()
        Logger.info('Click on the "New Tab"')
        handles.is_new_tab_button_click()
        Logger.info('Get the new window handle')
        all_handles = handles_utils.get_all_handles()
        for handle in all_handles:
            if handle != demoqa_handle:
                Logger.info('Open a new tab /sample')
                handles_utils.go_to_window(handle)
        sample_url = handles_utils.get_url()
        assert sample_url == ConfigTestData.\
            get_test_data_from_json('test_case_handles', 'sample_url'), 'No "/sample" in the url'

        Logger.info('Get text from a new tab /sample')
        sample = SamplePage()
        text_from_sample = sample.get_text_from_sample_page()
        assert text_from_sample == ConfigTestData.\
            get_test_data_from_json('test_case_handles', 'text_from_sample_page'), \
            'Sample page is not open'

        Logger.info('Close a tab')
        WebDriver().driver.close()
        handles_utils.go_to_window(demoqa_handle)
        handles.is_page_open()
        assert handles, 'Form Browser Windows is not open'

        Logger.info('From the left-hand menu, select "Elements" then select "Links"')
        handles.is_links_button_click()
        link = LinksPage()
        link.is_page_open()
        assert link, 'Form Links is not open'

        link_page = handles_utils.get_current_handle()
        Logger.info('Click on the "Home link"')
        link.is_button_link_to_home_click()
        all_link_handles = handles_utils.get_all_handles()
        Logger.info('Get the new window handle')
        for link_handle in all_link_handles:
            if link_handle != link_page:
                Logger.info('Open a new tab')
                handles_utils.go_to_window(link_handle)
        home_page_demoqa.is_page_open()
        assert home_page_demoqa, 'Demoqa main page is not open'

        Logger.info('Switching to the previous tab')
        handles_utils.go_to_window(link_page)
        link.is_page_open()
        assert link, 'Form Links is not open'
