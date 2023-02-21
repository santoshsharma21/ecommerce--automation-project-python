# import libraries
import time

import pytest
from pytest_lazyfixture import lazy_fixture

from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.custom_logger import LogGen


class TestCartPage(BaseTest):
    # logs
    log = LogGen.log_gen()

    # test methods
    @pytest.mark.parametrize(
        'new_login_data,product_data',
        [
            (lazy_fixture('get_new_login_data'), lazy_fixture('get_product_data')),
        ])
    def test_verify_order_total(self, new_login_data, product_data):
        self.log.info("========== test_verify_order_total START ==========")
        home_pg = HomePage(self.driver)
        customer_login_pg = home_pg.click_signin()
        self.log.info("clicked on sign in")
        customer_login_pg.login(new_login_data["new_email_id"], new_login_data["new_password"])
        self.log.info("entered email and password")
        home_pg = customer_login_pg.click_signin_button()
        self.log.info("login successful")
        search_result_pg = home_pg.search_product("sweatshirt")
        self.log.info("entered product name to search")
        product_details_pg = search_result_pg.click_on_product(cart=True)
        self.log.info("clicked on product")
        product_details_pg.add_product_to_cart(product_data["size"], product_data["colour"], product_data["quantity"])
        self.log.info("enterd size, color and quantity")
        cart_pg = product_details_pg.click_shopping_cart()
        self.log.info("clicked on shopping cart link")

        time.sleep(10)
        unit_price = cart_pg.get_unit_price()
        time.sleep(10)
        shipping_charge = cart_pg.get_shipping_charge()
        time.sleep(15)
        actual_order_price = cart_pg.get_order_price()

        expected_order_price = (unit_price * product_data["quantity"]) + (shipping_charge * product_data["quantity"])
        print(f"unit_price = {unit_price}, ship_charge = {shipping_charge}, order_price = {actual_order_price}")
        print(f"Actual amt = {actual_order_price}, Expected amt = {expected_order_price}")

        if actual_order_price == expected_order_price:
            assert True
            self.log.info("Test Passed")
        else:
            self.log.error("Test Failed")
            assert False

        self.log.info("========== test_verify_order_total END ==========")
