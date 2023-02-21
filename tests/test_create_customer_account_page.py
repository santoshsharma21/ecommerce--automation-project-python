# import libraries
import time

import pytest
from pytest_lazyfixture import lazy_fixture

from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.custom_logger import LogGen


class TestCustomerAccountPage(BaseTest):
    # logs
    log = LogGen.log_gen()

    # test methods
    @pytest.mark.parametrize(
        'login_data',
        [
            (lazy_fixture('generate_data_for_new_account')),
        ])
    def test_create_customer_account(self, login_data):
        self.log.info("========== test_create_customer_account START ==========")
        home_pg = HomePage(self.driver)
        create_customer_account_pg = home_pg.click_create_account()
        self.log.info("clicked on create account")
        create_customer_account_pg.create_new_customer_account(
            "sony", "kumar",
            login_data['email_id'],
            login_data['password'])
        self.log.info("entered first name, last name, email, password")
        my_account_pg = create_customer_account_pg.click_on_create_an_account_button()
        self.log.info("clicked on create account button")

        time.sleep(10)
        actual_text = my_account_pg.verify_new_account()
        expected_text = "Thank you for registering"
        print(f"Actual text = {actual_text}, Expected text = {expected_text}")

        if expected_text in actual_text:
            assert True
            self.log.info("Test Passed")
        else:
            self.log.error("Test Failed")
            assert False

        self.log.info("========== test_create_customer_account END ==========")
