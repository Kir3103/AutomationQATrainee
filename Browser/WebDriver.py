from Browser.BrowserFactory import BrowserFactory
from LogerUtils import Logger
from Pattern.MetaClassSingleton import MetaClassSingleton
from ConfigUtils import ConfigUtils


class WebDriver(metaclass=MetaClassSingleton):

    def __init__(self):
        Logger.info('Initialization driver')
        self.driver = BrowserFactory.get_driver_factory(ConfigUtils.
                                                        get_utils_from_json('browser_factory')[0])

    @staticmethod
    def get_driver():
        return WebDriver().driver

    def destroy(self):
        if self.driver is not None:
            self.driver.quit()
            WebDriver.clear()

    @staticmethod
    def is_switch_to():
        return WebDriver().driver.switch_to.default_content()
