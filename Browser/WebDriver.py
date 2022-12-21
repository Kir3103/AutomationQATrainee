from AutomationQATrainee.Browser.BrowserFactory import BrowserFactory
from AutomationQATrainee.Pattern.MetaClassSingleton import MetaClassSingleton
from AutomationQATrainee.Utils.ConfigUtils import ConfigUtils


class WebDriver(metaclass=MetaClassSingleton):

    def __init__(self):
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
