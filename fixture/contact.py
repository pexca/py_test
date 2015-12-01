class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_new_(self, contact):
        wd = self.app.wd
        # go to add contact page
        wd.find_element_by_link_text("add new").click()
        # input contact data
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # submit contact data
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def del_fstcontact(self):
        wd = self.app.wd
        #select first contact
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def add_address(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Moscow")
        wd.find_element_by_name("update").click()