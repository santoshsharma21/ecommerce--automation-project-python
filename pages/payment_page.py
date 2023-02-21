# import libraries
from selenium.webdriver.common.by import By

from pages import order_success_page
from pages.base_page import BasePage


class PaymentPage(BasePage):
    # page objects
    place_order_btn = (By.XPATH, "//button[@title='Place Order']")

    # constructor
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    # page actions
    def click_place_order(self):
        self.perform_click(self.place_order_btn)
        return order_success_page.OrderSuccessPage(self.driver)
