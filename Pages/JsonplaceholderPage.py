from AutomationQATrainee.Elements.BaseElement import BaseElements
from AutomationQATrainee.Pages.BasePage import BasePage


class JsonplaceholderPage(BasePage):
    locator_jsonplaceholder = BaseElements('//*[@id="hero"]')

    def __init__(self):
        super().__init__(unique_elem=JsonplaceholderPage.locator_jsonplaceholder)
