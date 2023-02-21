# import libraries
from selenium.webdriver.common.by import By

from pages import customer_login_page, my_wishlist_page
from pages import search_result_page
from pages import my_account_page
from pages.base_page import BasePage
from pages import create_customer_account_page


class HomePage(BasePage):
    # page objects
    signin = (By.XPATH, "//div[@class='panel header']//a[contains(text(),'Sign In')]")
    create_account = (By.XPATH, "//div[@class='panel header']//a[normalize-space()='Create an Account']")
    search_box = (By.XPATH, "//input[@id='search']")
    search_btn = (By.XPATH, "//button[@title='Search']")
    login_success = (By.XPATH, "//div[@class='panel header']//span[@class='logged-in'][normalize-space()='Welcome, "
                               "sony kumar!']")
    menu_btn = (By.XPATH, "//div[@class='panel header']//button[@type='button']")
    menu_options = (By.XPATH, "//li[@class='customer-welcome active']//div[@class='customer-menu']//ul[@class='header "
                              "links']/li")

    # constructor
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    # page actions
    def verify_home_page_title(self) -> str:
        title = self.get_title()
        return title

    def is_search_box_visible(self) -> bool:
        status = self.is_visible_and_enabled(self.search_box)
        return status

    def search_product(self, product_name: str):
        self.perform_send_value(self.search_box, product_name)
        self.perform_click(self.search_btn)
        return search_result_page.SearchResultPage(self.driver)

    def click_signin(self):
        self.perform_click(self.signin)
        return customer_login_page.CustomerLoginPage(self.driver)

    def verify_login(self) -> str:
        text = self.get_text(self.login_success)
        return text

    def click_create_account(self):
        self.perform_click(self.create_account)
        return create_customer_account_page.CreateCustomerAccountPage(self.driver)

    def select_my_account(self):
        self.perform_click(self.menu_btn)
        self.perform_select_by_visible_text(self.menu_options, "My Account", True)
        return my_account_page.MyAccountPage(self.driver)

    def select_my_wishlist(self):
        self.perform_click(self.menu_btn)
        self.perform_select_by_visible_text(self.menu_options, "My Wish List", True)
        return my_wishlist_page.MyWishlistPage(self.driver)

    # def select_signout(self):
    #     self.perform_click(self.menu_btn)
    #     self.perform_select_by_visible_text(self.menu_options, "Sign Out", True)
    #     return home_page.HomePage(self.driver)
