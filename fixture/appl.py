from selenium import webdriver
from fixture.session import SessionHandler
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:  # содержит все вспомогательные методы

    def __init__(self, browser, base_url):
        if browser == 'firefox':
            # initialize driver
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.session = SessionHandler(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except: return False

    def open_hp(self):
        wd = self.wd
        # open home page
        wd.get(self.base_url)

    def demolish(self):
        self.wd.quit()
