import pytest

from Browser.WebDriver import WebDriver
from LogerUtils import Logger
from ConfigUtils import ConfigUtils


@pytest.fixture(scope='function')
def get_webdriver():
    Logger.info('The website opens: ' + ConfigUtils.get_utils_from_json('url'))
    WebDriver.get_driver().get(ConfigUtils.get_utils_from_json('url'))
    yield WebDriver.get_driver()
    Logger.info('Stop the driver, clear and close the browser')
    WebDriver().destroy()
