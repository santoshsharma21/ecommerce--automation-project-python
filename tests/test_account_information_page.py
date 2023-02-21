# import libraries
import time

import pytest
from pytest_lazyfixture import lazy_fixture
from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.custom_logger import LogGen


class TestAccountInformationPage(BaseTest):
    # logs
    log = LogGen.log_gen()

    # test methods
    @pytest.mark.parametrize(
        'login_data, new_login_data',
        [
            (lazy_fixture('get_login_data'), lazy_fixture('generate_data_for_update_account')),
        ])
    def test_change_emailid(self, login_data, new_login_data):
        self.log.info("========== test_change_email_id START ==========")
        home_pg = HomePage(self.driver)
        customer_login_pg = home_pg.click_signin()
        self.log.info("clicked signin")
        customer_login_pg.login(login_data["email_id"], login_data["password"])
        self.log.info("entered email and password")
        home_pg = customer_login_pg.click_signin_button()
        self.log.info("clicked on signin button")
        my_account_pg = home_pg.select_my_account()
        self.log.info("selected my account")
        account_info_pg = my_account_pg.click_account_information()
        account_info_pg.change_email_id(new_login_data['new_email_id'], login_data["password"])
        # account_info_pg.change_email_id("new_email_id", "password")
        self.log.info("entered new emailid")
        customer_login_pg = account_info_pg.click_save()
        self.log.info("clicked on save button")

        time.sleep(10)
        actual_text = customer_login_pg.verify_email_update()
        expected_text = "You saved the account information"
        print(f"Actual text = {actual_text}, Expected text = {expected_text}")

        if expected_text in actual_text:
            assert True
            self.log.info("Test Passed")
        else:
            self.log.error("Test Failed")
            assert False

        self.log.info("========== test_change_email_id END ==========")

    @pytest.mark.parametrize(
        'login_data, new_login_data',
        [
            (lazy_fixture('get_login_data'), lazy_fixture('get_new_login_data')),
        ])
    def test_change_password(self, login_data, new_login_data):
        self.log.info("========== " + "test_change_password START ==========")
        home_pg = HomePage(self.driver)
        customer_login_pg = home_pg.click_signin()
        self.log.info("clicked signin")
        customer_login_pg.login(new_login_data['new_email_id'], login_data["password"])
        self.log.info("entered email and password")
        home_pg = customer_login_pg.click_signin_button()
        self.log.info("clicked on signin button")
        my_account_pg = home_pg.select_my_account()
        self.log.info("selected my account")
        accountt_info_pg = my_account_pg.click_account_information()
        accountt_info_pg.change_password(login_data["password"], new_login_data['new_password'],
                                         new_login_data['new_password'])
        self.log.info("entered new password")
        customer_login_pg = accountt_info_pg.click_save()
        self.log.info("clicked on save button")

        time.sleep(15)
        actual_text = customer_login_pg.verify_password_update()
        expected_text = "You saved the account information"
        print(f"Actual text = {actual_text}, Expected text = {expected_text}")

        if expected_text in actual_text:
            assert True
            self.log.info("Test Passed")
        else:
            self.log.error("Test Failed")
            assert False

        self.log.info("========== test_change_password END ==========")
