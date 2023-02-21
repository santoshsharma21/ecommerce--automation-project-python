# import libraries
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MyWishlistPage(BasePage):
    # page objects
    wishlist_confirmation_txt = (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")

    # constructor
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    # page actions
    def verify_add_to_wishlist(self) -> str:
        text = self.get_text(self.wishlist_confirmation_txt)
        return text
