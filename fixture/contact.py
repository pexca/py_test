from model.contact import *


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
        self.contacts_cache = None

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
        self.del_cont_by_idx(0)  # удалить элемент списка с индексом 0 == удалить первый элемент списка контактов

    def del_cont_by_idx(self, idx):
        wd = self.app.wd
        #select first contact
        self.select_cont_by_idx(idx)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contacts_cache = None

    def add_address(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("test")
        wd.find_element_by_name("update").click()
        self.contacts_cache = None

    def count(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))

    def mod_fstC(self):
        self.modify_idxcont(0)

    def modify_idxcont(self, idx, new_cData):
        wd = self.app.wd
        self.select_cont_by_idx(idx)
        # open edit form
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # fill some fields
        self.fill_contact_data(new_cData)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contacts_cache = None

    def select_fstC(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_cont_by_idx(self, idx):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[idx].click()

    contacts_cache = None

    def get_conts_lst(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            wd.find_element_by_link_text("home").click()
            self.contacts_cache = []
            for i in wd.find_elements_by_name('entry'):
                cells = i.find_elements_by_xpath('//div/div[4]/form[2]/table/tbody/tr/td')
                text = cells[2].text
                text1 = cells[1].text
                id = i.find_element_by_name('selected[]').get_attribute('value')
                self.contacts_cache.append(Contact(id=id, firstname=text, lastname=text1))
        return self.contacts_cache



