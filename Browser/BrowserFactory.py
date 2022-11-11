from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from LogerUtils import Logger


class BrowserFactory:
    @staticmethod
    def get_driver_factory(name_driver):
        if name_driver == 'chrome':
            options_for_chrome = chrome_options()
            options_for_chrome.add_argument('--start-maximized')
            options_for_chrome.add_argument('--incognito')
            options_for_chrome.add_argument('--lang=en-GB')
            Logger.info('The name of driver: Chrome')
            return webdriver.Chrome(ChromeDriverManager().install(), options=options_for_chrome)
        elif name_driver == 'firefox':
            options_for_firefox = firefox_options()
            options_for_firefox.add_argument('--start-maximized')
            options_for_firefox.add_argument('--incognito')
            options_for_firefox.add_argument('--lang=en-GB')
            Logger.info('The name of driver: Firefox')
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                     options=options_for_firefox)
