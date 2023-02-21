# import libraries
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderSuccessPage(BasePage):
    # page objects
    order_confirmation = (By.XPATH, "//span[@class='base']")

    # constructor
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    # page actions
    def verify_purchase(self) -> str:
        txt = self.get_text(self.order_confirmation)
        return txt
