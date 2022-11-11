import pytest
from Utils.config_webdriver import WebDriver
from Utils.config_utils import ConfigUtils


@pytest.fixture(scope='function')
def get_webdriver():
    driver = WebDriver().get_browser()
    driver.get(ConfigUtils().get_url_from_json())
    yield driver
    WebDriver().destroy()
    driver.quit()
