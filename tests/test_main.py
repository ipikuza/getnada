from selenium import webdriver
from core.content_builder import ContentBuilder
from methods.main_page import MainPage
from core.gmail_api_service import GmailApiService


class TestEmail:
    driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
    main_page = MainPage(driver)
    gmail_page = GmailApiService()
    content_builder = ContentBuilder()
    open_browser = driver.get("https://getnada.com/")
    assert "Nada - temp mail - fast and free" in driver.title

    def _init(self):
        self.gmail_page = GmailApiService()
        self.content_builder = ContentBuilder()


    def test_01_check_contents_of_sent_letter(self):
        """"
        Steps:
        1. Go to getnada.com
        2. Copy email in getnada.com
        3. Go to mail.google.com
        4. Send email with content from links
        5. Go back to getnada.com
        6. Check the received letter with contents of the links

        ER: Received a letter with the specified links
        """
        self.main_page.find_data_email()
        data_email = self.main_page.copy_data_email()
        links = self.content_builder.get_api_links()
        message = self.content_builder.create_message_content(links=links)
        self.gmail_page.send_message(to=data_email, subject="Test message", message_text=message)
        self.main_page.check_sent_letter()

