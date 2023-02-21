# import libraries
from selenium.webdriver.common.by import By
from pages import account_information_page, address_book_page, my_wishlist_page
from pages.base_page import BasePage


class MyAccountPage(BasePage):
    # page objects
    registration_status = (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")
    account_information = (By.XPATH, "//a[normalize-space()='Account Information']")
    address_book = (By.XPATH, "//a[normalize-space()='Address Book']")
    my_wishlist = (By.XPATH, "//li[@class='nav item']//a[normalize-space()='My Wish List']")

    # constructor
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    # page actions
    def verify_new_account(self) -> str:
        text = self.get_text(self.registration_status)
        return text

    def click_account_information(self):
        self.perform_click(self.account_information)
        return account_information_page.AccountInformationPage(self.driver)

    def click_address_book(self):
        self.perform_click(self.address_book)
        return address_book_page.AddressBookPage(self.driver)

    def click_my_wishlist(self):
        self.perform_click(self.my_wishlist)
        return my_wishlist_page.MyWishlistPage(self.driver)
