# import libraries
import time

import pytest
from pytest_lazyfixture import lazy_fixture
from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.custom_logger import LogGen


class TestProductDetailsPage(BaseTest):
    # logs
    log = LogGen.log_gen()

    # Test methods
    @pytest.mark.parametrize(
        'new_login_data,product_data',
        [
            (lazy_fixture('get_new_login_data'), lazy_fixture('get_product_data')),
        ])
    def test_add_to_cart(self, new_login_data, product_data):
        self.log.info("***** test_add_to_cart test START *****")
        home_pg = HomePage(self.driver)
        customer_login_pg = home_pg.click_signin()
        self.log.info("clicked on signin")
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

        time.sleep(5)
        actual_text = product_details_pg.verify_add_to_cart()
        expected_text = "You added Grayson Crewneck Sweatshirt to your shopping cart."
        print(f"Actual text = {actual_text}, Expected text = {expected_text}")

        if actual_text == expected_text:
            assert True
            self.log.info("Test Passed")
        else:
            self.log.error("Test Failed")
            assert False

        self.log.info("***** test_add_to_cart test END *****")

    @pytest.mark.parametrize(
        'new_login_data',
        [
            (lazy_fixture('get_new_login_data')),
        ])
    def test_add_to_wishlist(self, new_login_data):
        self.log.info("========== test_add_to_wish_list START ==========")
        home_pg = HomePage(self.driver)
        customer_login_pg = home_pg.click_signin()
        self.log.info("clicked on signin")
        customer_login_pg.login(new_login_data["new_email_id"], new_login_data["new_password"])
        self.log.info("entered email and password")
        home_pg = customer_login_pg.click_signin_button()
        self.log.info("login successful")
        search_result_pg = home_pg.search_product("sweatshirt")
        self.log.info("entered product name to search")
        product_details_pg = search_result_pg.click_on_product(wishlist=True)
        self.log.info("clicked on product")
        my_wishlist_pg = product_details_pg.add_product_to_wishlist()

        time.sleep(5)
        actual_text = my_wishlist_pg.verify_add_to_wishlist()
        expected_text = "Frankie Sweatshirt has been added to your Wish List"

        if expected_text in actual_text:
            assert True
            self.log.info("Test Passed")
        else:
            self.log.error("Test Failed")
            assert False

        self.log.info("========== test_add_to_wish_list END ==========")
