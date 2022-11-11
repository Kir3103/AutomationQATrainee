from Browser.WebDriver import WebDriver
from LogerUtils import Logger
from ConfigUtils import ConfigUtils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertUtils:

    @staticmethod
    def is_alert_visible():
        Logger.info('Check alert is visible')
        return WebDriverWait(WebDriver.get_driver(), ConfigUtils.
                             get_utils_from_json('default_timeout')).until(EC.alert_is_present())

    @staticmethod
    def accept_alert():
        alert = WebDriver.get_driver().switch_to.alert
        Logger.info('Accept alert')
        return alert.accept()

    @staticmethod
    def get_text_from_alert():
        alert = WebDriver.get_driver().switch_to.alert
        Logger.info('Get text from alert')
        return alert.text

    @staticmethod
    def send_text_to_alert(text):
        alert = WebDriver.get_driver().switch_to.alert
        alert.send_keys(text)
        Logger.info('Send text to alert')
        return alert.accept()
