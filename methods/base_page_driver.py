from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePageDriver():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()

    def divide(self, element):
        """
        We can transfer an element with a search method and a locator. For example:
        "id=testik".
        Values that can be taken by_what:
        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link text"
        PARTIAL_LINK_TEXT = "partial link text"
        NAME = "name"
        TAG_NAME = "tag name"
        CLASS_NAME = "class name"
        CSS_SELECTOR = "css selector"
        """
        by_what, element = element[:element.find('=')], element[element.find('=') + 1:]
        return by_what, element

    def waiting_for_an_item_to_appear(self, element):
        by_what, element = self.divide(element)
        self.wait.until(EC.presence_of_element_located((by_what, element)))

    def find_element(self, element, click_el=False, wait_el=True):
        if wait_el:
            self.waiting_for_an_item_to_appear(element)
        by_what, element = self.divide(element)
        element_xp = self.driver.find_element(by_what, element)
        if click_el:
            element_xp.click()
        return element_xp

    def get_text_selector(self, element):
        return self.find_element(element).text

    def refresh_browser(self):
        self.driver.refresh()
