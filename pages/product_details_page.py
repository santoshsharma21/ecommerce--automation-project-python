# import libraries
from selenium.webdriver.common.by import By

from pages import my_wishlist_page, cart_page
from pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    # page objects
    sizes = (By.XPATH, "//div[@class='swatch-attribute size']//div[@role='listbox']/div")
    colours = (By.XPATH, "//div[@class='swatch-attribute color']//div[@role='listbox']/div")
    quantity = (By.ID, "qty")
    add_to_cart_btn = (By.XPATH, "//span[normalize-space()='Add to Cart']")
    add_to_wish_list_btn = (By.XPATH, "//div[@class='product-addto-links']//span[contains(text(),'Add to Wish List')]")
    cart_confirmation = (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")
    shopping_cart = (By.XPATH, "//a[normalize-space()='shopping cart']")

    # constructor
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    # page actions
    def add_product_to_cart(self, size: str, colour: str, qty: int):
        self.click_by_matching_attribute_value(self.sizes, 'aria-label', size)
        self.click_by_matching_attribute_value(self.colours, 'aria-label', colour)
        self.perform_send_value(self.quantity, str(qty))
        self.perform_click(self.add_to_cart_btn)

    def verify_add_to_cart(self) -> str:
        text = self.get_text(self.cart_confirmation)
        return text

    def add_product_to_wishlist(self):
        self.perform_click(self.add_to_wish_list_btn)
        return my_wishlist_page.MyWishlistPage(self.driver)

    def click_shopping_cart(self):
        self.perform_click(self.shopping_cart)
        return cart_page.CartPage(self.driver)
