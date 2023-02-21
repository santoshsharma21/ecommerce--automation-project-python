# import libraries
import time

import pytest
from pytest_lazyfixture import lazy_fixture
from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.custom_logger import LogGen


class TestEndToEnd(BaseTest):
    # logs
    log = LogGen.log_gen()

    # test methods
    @pytest.mark.parametrize(
        'new_login_data,product_data',
        [
            (lazy_fixture('get_new_login_data'), lazy_fixture('get_product_data')),
        ])
    def test_end_to_end(self, new_login_data, product_data):
        self.log.info("========== test_end_to_end START ==========")
        home_pg = HomePage(self.driver)
        customer_login_pg = home_pg.click_signin()
        customer_login_pg.login(new_login_data["new_email_id"], new_login_data["new_password"])
        self.log.info("entered email and password")
        home_pg = customer_login_pg.click_signin_button()
        self.log.info("login successful")
        search_result_pg = home_pg.search_product("sweatshirt")
        self.log.info("entered product name")
        product_details_pg = search_result_pg.click_on_product(cart=True)
        self.log.info("clicked on product")
        product_details_pg.add_product_to_cart(product_data["size"], product_data["colour"], product_data["quantity"])
        self.log.info("product added to cart")
        cart_pg = product_details_pg.click_shopping_cart()
        shipping_pg = cart_pg.click_proceed_to_checkout()
        self.log.info("clicked on proceed to checkout button")
        time.sleep(10)
        payment_pg = shipping_pg.click_next_button()
        time.sleep(10)
        order_success_pg = payment_pg.click_place_order()
        self.log.info("clicked on place order button")
        time.sleep(10)
        actual_text = order_success_pg.verify_purchase()
        expected_text = "Thank you for your purchase!"
        print(f"Actual text = {actual_text}, Expected text = {expected_text}")

        if actual_text == expected_text:
            assert True
            self.log.info("Test Passed")
        else:
            self.log.error("Test Failed")
            assert False

        self.log.info("========== test_end_to_end END ==========")
