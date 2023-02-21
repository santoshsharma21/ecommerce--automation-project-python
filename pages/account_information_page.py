# import libraries
from selenium.webdriver.common.by import By
from pages import customer_login_page
from pages.base_page import BasePage


class AccountInformationPage(BasePage):
    # page objects
    change_email_checkbox = (By.XPATH, "//input[@id='change-email']")
    email = (By.ID, "email")
    password_for_email_change = (By.XPATH, "//input[@id='current-password']")

    change_password_checkbox = (By.XPATH, "//input[@id='change-password']")
    password_for_password_change = (By.XPATH, "//input[@id='current-password']")
    password = (By.XPATH, "//input[@id='password']")
    password_confirmation = (By.XPATH, "//input[@id='password-confirmation']")
    save_btn = (By.XPATH, "//span[normalize-space()='Save']")

    # constructor
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    # page actions
    def change_email_id(self, new_mail_id: str, password: str) -> None:
        self.perform_click(self.change_email_checkbox)
        self.perform_send_value(self.email, new_mail_id)
        self.perform_send_value(self.password_for_email_change, password)

    def change_password(self, current_password: str, new_password: str, confirm_password: str) -> None:
        self.perform_click(self.change_password_checkbox)
        self.perform_send_value(self.password_for_password_change, current_password)
        self.perform_send_value(self.password, new_password)
        self.perform_send_value(self.password_confirmation, confirm_password)

    def click_save(self):
        self.perform_click(self.save_btn)
        return customer_login_page.CustomerLoginPage(self.driver)
