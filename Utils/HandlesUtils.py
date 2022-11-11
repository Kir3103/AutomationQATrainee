from Browser.WebDriver import WebDriver
from LogerUtils import Logger


class HandlesUtils:

    @staticmethod
    def get_url():
        Logger.info('Get current url')
        return WebDriver.get_driver().current_url

    @staticmethod
    def get_current_handle():
        Logger.info('Get current handle')
        return WebDriver.get_driver().current_window_handle

    @staticmethod
    def get_all_handles():
        Logger.info('Get all handles')
        return WebDriver.get_driver().window_handles

    @staticmethod
    def go_to_window(handle):
        Logger.info('Go to new window')
        return WebDriver.get_driver().switch_to.window(handle)
