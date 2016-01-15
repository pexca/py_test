from model.contact import *
import re


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
        # select idx contact
        self.select_cont_by_idx(idx)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contacts_cache = None

    def add_address(self):
        wd = self.app.wd
        self.app.open_hp()                      #
        wd.find_element_by_css_selector('img[alt="Edit"]').click()
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("test")
        wd.find_element_by_name("update").click()
        self.contacts_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_hp()
        return len(wd.find_elements_by_name("selected[]"))

    def mod_fstC(self):
        self.modify_idxcont(0)

    def modify_idxcont(self, idx, new_cData):
        wd = self.app.wd
        self.select_cont_by_idx(idx)
        # open edit form
        wd.find_element_by_css_selector('img[alt="Edit"]').click()
        # fill some fields
        self.fill_contact_data(new_cData)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contacts_cache = None

    def select_fstC(self):
        wd = self.app.wd
        self.app.open()
        wd.find_element_by_name("selected[]").click()

    def select_cont_by_idx(self, idx):
        wd = self.app.wd
        self.app.open_hp()  #
        wd.find_elements_by_name("selected[]")[idx].click()

    contacts_cache = None

    def get_conts_lst(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.app.open_hp()
            self.contacts_cache = []
            for i in wd.find_elements_by_name('entry'):
                cells = i.find_elements_by_tag_name('td')
                # cells = i.find_elements_by_xpath('//div/div[4]/form[2]/table/tbody/tr/td')
                text = cells[2].text
                text1 = cells[1].text
                id = cells[0].find_element_by_tag_name('input').get_attribute('value')
                # id = i.find_element_by_name('selected[]').get_attribute('value')
                all_phnums = cells[5].text
                address = cells[3].text
                emails = cells[4].text
                self.contacts_cache.append(Contact(id=id, firstname=text, lastname=text1,
                                                   all_phnums_from_hp=all_phnums, address=address, emails=emails))
        return list(self.contacts_cache)

    def open_cont_edit_idx(self, idx):
        wd = self.app.wd
        self.app.open_hp()
        row = wd.find_elements_by_name('entry')[idx]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_cont_view_idx(self, idx):
        wd = self.app.wd
        self.app.open_hp()
        row = wd.find_elements_by_name('entry')[idx]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_cont_info_from_edit_page(self, idx):
        wd = self.app.wd
        self.open_cont_edit_idx(idx)
        fname = wd.find_element_by_name('firstname').get_attribute('value')
        lname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        hphone = wd.find_element_by_name('home').get_attribute('value')
        wphone = wd.find_element_by_name('work').get_attribute('value')
        sphone = wd.find_element_by_name('phone2').get_attribute('value')
        mphone = wd.find_element_by_name('mobile').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        return Contact(firstname=fname, lastname=lname, id=id, hphone=hphone, wphone=wphone,
                       sphone=sphone, mphone=mphone, address=address, email=email, email2=email2, email3=email3)

    def get_cont_from_viewpage(self, idx):
        wd = self.app.wd
        self.open_cont_view_idx(idx)
        text = wd.find_element_by_id('content').text
        hphone = re.search('H: (.*)', text).group(1)
        wphone = re.search('W: (.*)', text).group(1)
        mphone = re.search('M: (.*)', text).group(1)
        sphone = re.search('P: (.*)', text).group(1)
        return Contact(hphone=hphone, wphone=wphone, sphone=sphone, mphone=mphone)

    def del_cont_byid(self, id):
        wd = self.app.wd
        self.app.open_hp()
        self.select_cont_byid(id)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contacts_cache = None

    def select_cont_byid(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def modify_cont_byid(self, id):
        wd = self.app.wd
        self.app.open_hp()
        self.select_cont_byid(id)
        wd.find_element_by_css_selector('img[alt="Edit"]').click()
        self.input('lastname', 'new lastname')
        wd.find_element_by_name("update").click()
        self.contacts_cache = None
