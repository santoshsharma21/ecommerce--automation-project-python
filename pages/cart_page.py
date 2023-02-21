# import libraries
from selenium.webdriver.common.by import By
from pages import shipping_page
from pages.base_page import BasePage


class CartPage(BasePage):
    # page objects
    unit_price = (By.XPATH, "//td[@class='col price']//span[@class='cart-price']")
    sub_total = (By.XPATH, "//td[@class='col subtotal']//span[@class='cart-price']")
    shipping_charges = (By.CSS_SELECTOR, "span[data-th='Shipping']")
    total_price = (By.XPATH, "//tr[@class='grand totals']//td[@class='amount']/strong/span")
    proceed_to_checkout_btn = (By.XPATH, "//button[@data-role='proceed-to-checkout']")

    # Constructor
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    # page action
    def get_unit_price(self) -> float:
        amt = self.get_text(self.unit_price)
        unt_price = amt.split("$")[1]
        return float(unt_price)

    def get_sub_total(self) -> float:
        amt = self.get_text(self.sub_total)
        sub_tt = amt.split("$")[1]
        return float(sub_tt)

    def get_shipping_charge(self) -> float:
        amt = self.get_text(self.shipping_charges)
        ship_charge = amt.split("$")[1]
        return float(ship_charge)

    def get_order_price(self) -> float:
        amt = self.get_text(self.total_price)
        tt_price = amt.split("$")[1]
        return float(tt_price)

    def click_proceed_to_checkout(self):
        self.perform_click(self.proceed_to_checkout_btn)
        return shipping_page.ShippingPage(self.driver)
