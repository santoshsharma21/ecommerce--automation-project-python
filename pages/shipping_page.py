# import libraries
from selenium.webdriver.common.by import By

from pages import payment_page
from pages.base_page import BasePage


class ShippingPage(BasePage):
    # page objects
    next_btn = (By.XPATH, "//button[@class='button action continue primary']")

    # constructor
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    # page actions
    def click_next_button(self):
        self.perform_click(self.next_btn)
        return payment_page.PaymentPage(self.driver)
