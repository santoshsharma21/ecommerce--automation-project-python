# import libraries
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
# from pages import create_customer_account_page
from pages import home_page


class CustomerLoginPage(BasePage):
    # page objects
    email = (By.ID, "email")
    password = (By.ID, "pass")
    signin_btn = (By.XPATH, "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]")
    login_failed = (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")
    create_acct_btn = (By.CSS_SELECTOR, "a[class='action create primary'] span")
    acct_edit_confirm_msg = (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")

    # constructor
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    # page actions
    def login(self, email: str, password: str) -> None:
        self.perform_send_value(self.email, email)
        self.perform_send_value(self.password, password)

    def click_signin_button(self):
        self.perform_click(self.signin_btn)
        return home_page.HomePage(self.driver)

    # def click_to_create_account(self):
    #     self.perform_click(self.create_acct_btn)
    #     return create_customer_account_page.CreateCustomerAccountPage(self.driver)

    def verify_email_update(self) -> str:
        text = self.get_text(self.acct_edit_confirm_msg)
        return text

    def verify_password_update(self) -> str:
        text = self.get_text(self.acct_edit_confirm_msg)
        return text
