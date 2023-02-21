# import libraries
import time

import pytest
from pytest_lazyfixture import lazy_fixture

from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.custom_logger import LogGen


class TestAddressBookPage(BaseTest):
    # logs
    log = LogGen.log_gen()

    # test methods
    @pytest.mark.parametrize(
        'new_login_data,address_data',
        [
            (lazy_fixture('get_new_login_data'), lazy_fixture('get_address_data')),
        ])
    def test_add_address(self, new_login_data, address_data):
        self.log.info("========== test_add_address START ==========")
        home_pg = HomePage(self.driver)
        customer_login_pg = home_pg.click_signin()
        # customer_login_pg.login(login_data["email_id"], login_data["password"])
        customer_login_pg.login(new_login_data["new_email_id"], new_login_data["new_password"])
        home_pg = customer_login_pg.click_signin_button()
        self.log.info("login successful")
        my_account_pg = home_pg.select_my_account()
        self.log.info("selected my account")
        address_book_pg = my_account_pg.click_address_book()
        self.log.info("clicked on address book")
        address_book_pg.add_address(address_data["telephone"], address_data["house"], address_data["city"],
                                    address_data["country"], address_data["region"], address_data["zip_code"])
        self.log.info("entered details to add address")

        time.sleep(10)
        actual_text = address_book_pg.verify_add_address()
        expected_text = "You saved the address."
        print(f"Actual text = {actual_text}, Expected text = {expected_text}")

        if expected_text in actual_text:
            assert True
            self.log.info("Test Passed")
        else:
            self.log.error("Test Failed")
            assert False

        self.log.info("========== test_add_address END ==========")
