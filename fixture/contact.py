class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_new_(self, contact):
        wd = self.app.wd
        # go to add contact page
        wd.find_element_by_link_text("add new").click()
        # input contact data
        self.fill_contact_data(contact)
        # submit contact data
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_data(self, contact):
        wd = self.app.wd
        self.input('firstname', contact.firstname)
        self.input('lastname', contact.lastname)
        self.input('email', contact.email)

    def input(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def del_fstcontact(self):
        wd = self.app.wd
        #select first contact
        self.select_fstC()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def add_address(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("test")
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def mod_fstC(self, new_cData):
        wd = self.app.wd
        self.select_fstC()
        # open edit form
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # fill some fields
        self.fill_contact_data(new_cData)
        # submit modification
        wd.find_element_by_name("update").click()

    def select_fstC(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
