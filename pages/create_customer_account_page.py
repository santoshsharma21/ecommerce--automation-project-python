# import libraries
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages import my_account_page


class CreateCustomerAccountPage(BasePage):
    # page objects
    first_name = (By.ID, "firstname")
    last_name = (By.ID, "lastname")
    email_address = (By.ID, "email_address")
    password = (By.ID, "password")
    password_confirmation = (By.ID, "password-confirmation")
    create_account_btn = (By.CSS_SELECTOR, "button[title='Create an Account'] span")

    # constructor
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    # page actions
    def create_new_customer_account(self, fname: str, lname: str, email: str, password: str) -> None:
        self.perform_send_value(self.first_name, fname)
        self.perform_send_value(self.last_name, lname)
        self.perform_send_value(self.email_address, email)
        self.perform_send_value(self.password, password)
        self.perform_send_value(self.password_confirmation, password)

    def click_on_create_an_account_button(self):
        self.perform_click(self.create_account_btn)
        return my_account_page.MyAccountPage(self.driver)
