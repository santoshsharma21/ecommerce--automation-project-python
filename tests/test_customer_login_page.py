# import libraries
import pytest
from pytest_lazyfixture import lazy_fixture
from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.custom_logger import LogGen


class TestCustomerLoginPage(BaseTest):
    # logs
    log = LogGen.log_gen()

    @pytest.mark.parametrize(
        'new_login_data',
        [
            (lazy_fixture('get_new_login_data')),
        ])
    def test_login(self, new_login_data):
        self.log.info("========== test_login START ==========")
        home_pg = HomePage(self.driver)
        customer_login_pg = home_pg.click_signin()
        self.log.info("clicked on signin")
        customer_login_pg.login(new_login_data["new_email_id"], new_login_data["new_password"])
        self.log.info("entered email and password")
        home_pg = customer_login_pg.click_signin_button()
        self.log.info("clicked login button")

        actual_text = home_pg.verify_login()
        expected_text = "Welcome, sony kumar!"
        print(f"Actual text = {actual_text}, Expected text = {expected_text}")

        if expected_text == actual_text:
            assert True
            self.log.info("login successful")
            self.log.info("Test Passed")
        else:
            self.log.info("login unsuccessful")
            self.log.error("Test Failed")
            assert False

        self.log.info("========== test_login END ==========")
