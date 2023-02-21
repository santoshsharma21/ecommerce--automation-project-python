# import libraries
import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.custom_logger import LogGen


class TestHomePage(BaseTest):
    # logs
    log = LogGen.log_gen()

    # test methods
    def test_home_page_title(self):
        self.log.info("========== test_home_page_title START ==========")
        home_pg = HomePage(self.driver)
        actual_title = home_pg.verify_home_page_title()
        expected_title = "Home Page - Magento eCommerce"
        self.log.info("verifying home page title")

        if expected_title in actual_title:
            assert True
            self.log.info("Test Passed")
        else:
            self.log.error("Test Failed")
            assert False

        self.log.info("========== test_home_page_title END ==========")

    @pytest.mark.xfail(reason="deliberate fail")
    def test_validate_search_box(self):
        self.log.info("========== test_validate_search_box START ==========")
        home_pg = HomePage(self.driver)
        status = home_pg.is_search_box_visible()
        self.log.info("verifying search box visibility")

        # make test failed
        if status:
            self.log.info("Test Failed")
            assert False

        self.log.info("========== test_validate_search_box END ==========")
