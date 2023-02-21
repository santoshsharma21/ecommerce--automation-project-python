# import libraries
import pytest
from pytest_lazyfixture import lazy_fixture
from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.custom_logger import LogGen


class TestSearchResultPage(BaseTest):
    # logs
    log = LogGen.log_gen()

    # test methods
    @pytest.mark.parametrize(
        'new_login_data',
        [
            (lazy_fixture('get_new_login_data')),
        ])
    def test_product_availability(self, new_login_data):
        self.log.info("========== test_product_availability START ==========")
        home_pg = HomePage(self.driver)
        customer_login_pg = home_pg.click_signin()
        self.log.info("clicked on signin")
        customer_login_pg.login(new_login_data["new_email_id"], new_login_data["new_password"])
        self.log.info("entered email and password")
        home_pg = customer_login_pg.click_signin_button()
        self.log.info("login successful")
        search_result_pg = home_pg.search_product("sweatshirt")
        self.log.info("entered product name to search")
        status = search_result_pg.is_product_availabel()
        self.log.info("verifying product availability")

        if status:
            assert True
            self.log.info("Test Passed")
        else:
            self.log.error("Test Failed")
            assert False

        self.log.info("========== test_product_availability END ==========")
