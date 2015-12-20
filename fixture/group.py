from model.group import *


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_gp(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_gp()
        # init. groups creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_gform(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_gp()
        self.group_cache = None

    def fill_gform(self, group):
        wd = self.app.wd
        self.change_field_val("group_name", group.name)
        self.change_field_val("group_header", group.header)
        self.change_field_val("group_footer", group.footer)

    def change_field_val(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_gp(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name('new')) > 0):
            wd.find_element_by_link_text("groups").click()

    def del_fst_group(self):
        self.del_idxgroup(0)

    def sel_idxgroup(self, idx):  # select group with random index
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[idx].click()

    def del_idxgroup(self, idx):  # delete group with random index 'idx'
        wd = self.app.wd
        self.open_gp()
        # select first group
        # submit group deletion
        self.sel_idxgroup(idx)
        wd.find_element_by_name("delete").click()
        wd.find_element_by_link_text("group page").click()
        self.group_cache = None

    def select_fst_g(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_fstg(self):
        self.modify_idxgroup(0)

    def modify_idxgroup(self, idx, new_gData):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.sel_idxgroup(idx)
        wd.find_element_by_name("edit").click()
        self.fill_gform(new_gData)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("group page").click()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_gr_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_gp()
            self.group_cache = []
            for i in wd.find_elements_by_css_selector('span.group'):
                text = i.text  # обращение к свойству "text" элемента
                id = i.find_element_by_name('selected[]').get_attribute('value')
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

