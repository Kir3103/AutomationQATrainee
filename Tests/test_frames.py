from LogerUtils import Logger
from Models.TextCompareModel import TextCompareModel
from Pages.AlertsFrameWindowsPage import AlertsFrameWindowPage
from Pages.FramesPage import FramesPage
from Pages.HomePage import HomePage
from Pages.NestedFramesPage import NestedFramesPage
from ConfigTestData import ConfigTestData


class TestFrames:

    def test_nested_frames(self, get_webdriver):

        Logger.info('Go to the homepage')
        home_page_demoqa = HomePage()
        home_page_demoqa.is_page_open()
        assert home_page_demoqa, 'Demoqa main page is not open'

        Logger.info('Click on the button "Alerts, Frame & Windows button. '
                    'On the page that opens, click on Nested Frames in the left-hand menu"')
        home_page_demoqa.select_alerts_frames_windows()
        alerts_frame_windows = AlertsFrameWindowPage()
        alerts_frame_windows.is_select_button_nested_frames()
        nested_iframes = NestedFramesPage()
        nested_iframes.is_page_open()
        assert nested_iframes, 'Nested Frames form is not open'

        Logger.info('See if the frame text is visible on the page')
        Logger.info('Get data from json file')
        text_from_frames_parent = ConfigTestData.get_test_data_from_json('test_case_nested_frames',
                                                                         'nested_frames')[0]
        text_from_frames_child = ConfigTestData.get_test_data_from_json('test_case_nested_frames',
                                                                        'nested_frames')[1]
        expected_text_from_model_iframes = TextCompareModel(text_from_frames_parent,
                                                            text_from_frames_child)
        assert nested_iframes.is_text_iframe_visible() == expected_text_from_model_iframes, \
            'Text from Nested Frames does not visible'

        Logger.info('Select Frames from the left-hand menu')
        nested_iframes.return_to_default_iframe()
        alerts_frame_windows.is_select_button_frames()
        iframes = FramesPage()
        iframes.is_page_open()
        assert iframes, 'Frames form is not open'

        Logger.info('Comparing text from different frames')
        text_from_up_frame = iframes.get_text_top_frame()
        nested_iframes.return_to_default_iframe()
        text_from_down_frame = iframes.get_text_down_frame()
        Logger.info('Get data from json file')
        expected_text_from_frame = ConfigTestData.\
            get_test_data_from_json('test_case_nested_frames', 'frames')
        assert text_from_down_frame in expected_text_from_frame \
               and text_from_up_frame in expected_text_from_frame, \
            'Different text in page or text does not equal "This is a sample page"'
