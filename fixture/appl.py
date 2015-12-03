from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHandler
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:  # содержит все вспомогательные методы

    def __init__(self):
        # initialize driver
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)
        self.session = SessionHandler(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except: return False

    def open_hp(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/")

    def demolish(self):
        self.wd.quit()
