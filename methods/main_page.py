from methods.base_page_driver import BasePageDriver


class MainPage(BasePageDriver):
    def __init__(self, driver):
        BasePageDriver.__init__(self, driver)


############################################    XPath GetNada Email page     ##########################################
        self.input_email = "xpath= //span[@class='address what_to_copy']"
        self.gmail = "xpath= //div[text()='ipqa.autotest@gmail.com']"
        self.link_cat = "xpath= //div[@dir='ltr']/a[contains(@href, 'purr')]"
        self.link_dog = "xpath= //div[@dir='ltr']/a[contains(@href, 'dog')]"
        self.link_fox = "xpath= //div[@dir='ltr']/a[contains(@href, 'fox')]"


    def find_data_email(self):
        self.find_element(element=self.input_email)

    def copy_data_email(self):
        data_email = self.get_text_selector(element=self.input_email)
        return data_email

    def check_sent_letter(self):
        self.find_element(element=self.gmail, click_el=True)
        self.find_element(element=self.link_cat)
        self.find_element(element=self.link_dog)
        self.find_element(element=self.link_fox)

    def refresh_page(self):
        self.refresh_browser()
        self.driver.implicitly_wait(2)
        self.find_element(element=self.input_email)