# import libraries
import os.path
import pytest
from selenium import webdriver
from configurations.config import ConfigData
from datetime import datetime
import time
import pandas as pd

from dataprovider.test_data_provider import DataProviders
from utilities.utils import Utils


@pytest.fixture(params=["chrome"], scope="function")
def browser_setup(request):
    global web_driver
    if request.param == "chrome":
        web_driver = webdriver.Chrome()

    request.cls.driver = web_driver
    # open url
    web_driver.get(ConfigData.BASE_URL)
    # maximize window
    web_driver.maximize_window()
    yield
    # quit windows
    web_driver.quit()


@pytest.fixture(scope='package')
def generate_data_for_new_account():
    rand_str = Utils().random_data_generator(size=7)
    email_id = rand_str + "@gmail.com"
    password = "password@" + rand_str
    df = pd.read_csv("./testdata/file_new_account_details.csv")
    # for jenkins
    # df = pd.read_csv("./ecommerce-project/testdata/file_new_account_details.csv")
    df["first_name"] = "sony"
    df["last_name"] = "kumar"
    df["email_id"] = email_id
    df["password"] = password
    df.to_csv("./testdata/file_new_account_details.csv")
    # jenkins
    # df.to_csv("./ecommerce-project/testdata/file_new_account_details.csv")
    data_dict = {"email_id": email_id, "password": password}
    return data_dict


@pytest.fixture(scope='package')
def generate_data_for_update_account():
    rand_str = Utils().random_data_generator(size=5)
    new_email_id = rand_str + "@gmail.com"
    new_password = "password@" + rand_str
    df = pd.read_csv("./testdata/file_update_account_details.csv")
    # for jenkins
    # df = pd.read_csv("./ecommerce-project/testdata/file_update_account_details.csv")
    df["new_email_id"] = new_email_id
    df["new_password"] = new_password
    df.to_csv("./testdata/file_update_account_details.csv")
    # jenkins
    # df.to_csv("./ecommerce-project/testdata/file_update_account_details.csv")
    data_dict = {"new_email_id": new_email_id, "new_password": new_password}
    return data_dict


@pytest.fixture
def get_login_data():
    login_data_dict = DataProviders().get_test_data("./testdata/file_new_account_details.csv")
    # for jenkins
    # login_data_dict = DataProviders().get_test_data(
    #     "./ecommerce-project/testdata/file_new_account_details.csv")
    return login_data_dict


@pytest.fixture
def get_new_login_data():
    new_login_data_dict = DataProviders().get_test_data("./testdata/file_update_account_details.csv")
    # for jenkins
    # new_login_data_dict = DataProviders().get_test_data(
    #     "./ecommerce-project/testdata/file_update_account_details.csv")
    return new_login_data_dict


@pytest.fixture
def get_address_data():
    address_data_dict = DataProviders().get_test_data("./testdata/file_address_details.csv")
    # for jenkins
    # address_data_dict = DataProviders().get_test_data(
    #     "./ecommerce-project/testdata/file_address_details.csv")
    return address_data_dict


@pytest.fixture
def get_product_data():
    product_data_dict = DataProviders().get_test_data("./testdata/file_product_details.csv")
    # for jenkins
    # product_data_dict = DataProviders().get_test_data(
    #     "./ecommerce-project/testdata/file_product_details.csv")
    return product_data_dict

# reorder pytest test collection
def pytest_collection_modifyitems(items):
    """Modifies test items in place to ensure test classes run in a given order."""
    CLASS_ORDER = ["TestAccountInformationPage", "TestAddressBookPage", "TestCartPage", "TestCustomerLoginPage",
                   "TestEndToEnd", "TestHomePage", "TestMyWishListPage",
                   "TestProductDetailsPage", "TestSearchResultPage"]

    class_mapping = {item: item.cls.__name__ for item in items}

    sorted_items = items.copy()
    # Iteratively move tests of each class to the end of the test queue
    for class_ in CLASS_ORDER:
        sorted_items = [it for it in sorted_items if class_mapping[it] != class_] + [
            it for it in sorted_items if class_mapping[it] == class_]
    items[:] = sorted_items


# HTML-Report
# methods takes screenshot
def take_screenshot(file, root_dir):
    dt = datetime.now().strftime("%d.%m.%Y_%H.%M.%S")
    img_file = file + "_" + dt + ".png"
    dest_file = os.path.join(root_dir, img_file)
    web_driver.get_screenshot_as_file(dest_file)
    return img_file


# change report title
def pytest_html_report_title(report):
    report.title = "Ecommerce Test Report"

def pytest_configure(config):
    if hasattr(config, '_metadata'):
        # noinspection PyProtectedMember
        config._metadata["Tester"] = "Santosh Sharma"

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call" or report.when == "setup":
        # always add url to report
        extra.append(pytest_html.extras.url("https://magento.softwaretestingboard.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            rd = os.path.dirname(item.config.option.htmlpath)
            file = report.nodeid.replace("::", "_")
            img_file = take_screenshot(file, rd)
            if img_file:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' %img_file
            extra.append(pytest_html.extras.html(html))
        report.extra = extra
