from Pages.BasePage import BasePage
from Elements.BaseElement import BaseElements
from Elements.Button import Button
from StringUtils import StringUtils


class AlertPage(BasePage):
    locator_alert_form_button_see = '//*[@id="alertButton"]'
    locator_alert_form_button_confirm = '//*[@id="confirmButton"]'
    locator_alert_confirm = '//*[@id="confirmResult"]'
    locator_alert_form_button_box = '//*[@id="promtButton"]'
    locator_text_from_alert_form_button_box = '//*[@id="promptResult"]'

    def __init__(self):
        self.alert_form_button_see = Button(AlertPage.locator_alert_form_button_see,
                                            '"Click Button to see alert"')
        self.alert_form_button_confirm = Button(AlertPage.locator_alert_form_button_confirm,
                                                '"On button click, confirm box will appear"')
        self.alert_confirm = BaseElements(AlertPage.locator_alert_confirm,
                                          '"Do you confirm action?"')
        self.alert_form_button_box = Button(AlertPage.locator_alert_form_button_box,
                                            '"On button click, prompt box will appear"')
        self.text_from_alert_form_button_box = BaseElements(AlertPage.
                                                            locator_text_from_alert_form_button_box,
                                                            'Alert form button box')
        super().__init__(unique_elem=None, name_log='Alert')

    def is_alert_form_button_see_click(self):
        return self.alert_form_button_see.click_script()

    def check_alert_closed(self):
        return self.alert_form_button_see.element_is_clickable()

    def is_alert_form_button_confirm_click(self):
        return self.alert_form_button_confirm.click_script()

    def get_text_from_alert_confirm(self):
        return self.alert_confirm.get_text()

    def is_alert_form_button_box_click(self):
        return self.alert_form_button_box.click_script()

    def get_text_from_alert_form_button_box(self):
        text_from_alert = self.text_from_alert_form_button_box.get_text()
        return StringUtils.get_text_with_slice(text_from_alert, 2)
