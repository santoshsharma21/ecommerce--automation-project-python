# Import libraries
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    wait_time = 25

    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.wait_time)

    def perform_click(self, by_locator) -> None:
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def perform_send_value(self, by_locator, value) -> None:
        self.wait.until(EC.presence_of_element_located(by_locator)).clear()
        self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(value)

    def perform_mouse_hover_click(self, by_locator) -> None:
        act = ActionChains(self.driver)
        web_element = self.wait.until(EC.presence_of_element_located(by_locator))
        act.move_to_element(web_element).click().perform()

    def is_displayed(self, by_locator) -> bool:
        flag = self.wait.until(EC.presence_of_element_located(by_locator)).is_displayed()
        return flag

    def is_visible_and_enabled(self, by_locator) -> bool:
        return self.wait.until(EC.element_to_be_clickable(by_locator))

    def get_title(self) -> str:
        return self.driver.title

    def title_contains(self, title) -> bool:
        flag = self.wait.until(EC.title_contains(title))
        return flag

    def match_current_url(self, url) -> bool:
        status = self.wait.until(EC.url_contains(url))
        return status

    def get_current_url(self) -> str:
        url = self.driver.current_url
        return url

    def get_attribute_value(self, by_locator, attribute) -> str:
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        return element.get_attribute(attribute)

    def get_text(self, by_locator) -> str:
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        return element.text

    def check_text_in_element(self, by_locator, text) -> bool:
        flag = self.wait.until(EC.text_to_be_present_in_element(by_locator, text))
        return flag

    def click_by_matching_attribute_value(self, by_locator, attribute, value) -> None:
        elements = self.wait.until(EC.presence_of_all_elements_located(by_locator))
        for element in elements:
            txt = element.get_attribute(attribute)
            if txt == value:
                self.perform_click(element)
                break

    def perform_select_by_visible_text(self, by_locator, text, bootstrap=False) -> None:
        if bootstrap:
            elements = self.wait.until(EC.presence_of_all_elements_located(by_locator))
            for element in elements:
                if element.text == text:
                    element.click()
                    break
        elif not bootstrap:
            element = self.wait.until(EC.presence_of_element_located(by_locator))
            drop_down = Select(element)
            drop_down.select_by_visible_text(text)
