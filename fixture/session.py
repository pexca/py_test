class SessionHandler:

    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_hp()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in(): # проверка количества элементов Logout на странице
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.logged_in_as(username):
                return  # what does it do exactly?
            else: self.logout()
        self.login(username, password)

    def logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "("+username+")"