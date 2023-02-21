# import libraries
from selenium.webdriver.common.by import By

from pages import product_details_page
from pages.base_page import BasePage


class SearchResultPage(BasePage):
    # page objects
    product_result = (By.XPATH, "//img[@alt='Grayson Crewneck Sweatshirt ']")
    product_for_wishlist = (By.XPATH, "//img[@alt='Frankie  Sweatshirt']")
    product_for_cart = (By.XPATH, "//img[@alt='Grayson Crewneck Sweatshirt ']")

    # constructor
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    # page actions
    def is_product_availabel(self) -> bool:
        status = self.is_displayed(self.product_result)
        return status

    def click_on_product(self, cart: bool = False, wishlist: bool = False):
        if cart:
            self.perform_mouse_hover_click(self.product_for_cart)
        elif wishlist:
            self.perform_mouse_hover_click(self.product_for_wishlist)
        return product_details_page.ProductDetailsPage(self.driver)

    def sort_by_price(self):
        pass
