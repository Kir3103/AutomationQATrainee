import pytest

from AutomationQATrainee.Browser.WebDriver import WebDriver
from AutomationQATrainee.Utils.ConfigUtils import ConfigUtils


@pytest.fixture(scope='function')
def get_webdriver():
    WebDriver.get_driver().get(ConfigUtils.get_utils_from_json('url'))
    yield WebDriver.get_driver()
    WebDriver().destroy()
