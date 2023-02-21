# import libraries
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddressBookPage(BasePage):
    # page objects
    new_address_btn = (By.XPATH, "//button[@title='Add New Address']")
    telephone = (By.ID, "telephone")
    street_1 = (By.ID, "street_1")
    city = (By.ID, "city")
    country_drop_down = (By.XPATH, "//select[@id='country']")
    region_drop_down = (By.XPATH, "//select[@id='region_id']")
    zip = (By.ID, "zip")
    billing_address_checkbox = (By.ID, "primary_billing")
    shipping_address_checkbox = (By.ID, "primary_shipping")
    save_address_btn = (By.XPATH, "//span[normalize-space()='Save Address']")
    address_confirmation = (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")

    # constructor
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    def input_address_details(self, tele_no: int, street_add: str, city: str, country: str, region: str, zip_code: int):
        self.perform_send_value(self.telephone, str(tele_no))
        self.perform_send_value(self.street_1, street_add)
        self.perform_send_value(self.city, city)
        self.perform_select_by_visible_text(self.country_drop_down, country)
        self.perform_select_by_visible_text(self.region_drop_down, region)
        self.perform_send_value(self.zip, str(zip_code))
        # self.perform_click(self.billing_address_checkbox)
        # self.perform_click(self.shipping_address_checkbox)
        self.perform_click(self.save_address_btn)

    def add_address(self, tele_no: int, street_add: str, city: str, country: str, region: str, zip_code: int):
        time.sleep(10)
        url = self.get_current_url()
        if url == "https://magento.softwaretestingboard.com/customer/address/new/":
            self.input_address_details(tele_no, street_add, city, country, region, zip_code)
        elif url == "https://magento.softwaretestingboard.com/customer/address/":
            self.perform_click(self.new_address_btn)
            self.input_address_details(tele_no, street_add, city, country, region, zip_code)

    def verify_add_address(self) -> str:
        return self.get_text(self.address_confirmation)
