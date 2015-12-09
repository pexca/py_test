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
        if not (wd.current_url.endswith("\group") and len(wd.find_elements_by_name('new')) > 0):
            wd.find_element_by_link_text("groups").click()

    def del_fst_group(self):
        wd = self.app.wd
        self.open_gp()
        #select first group
        #submit group deletion
        self.select_fst_g()
        wd.find_element_by_name("delete").click()
        wd.find_element_by_link_text("group page").click()

    def select_fst_g(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_fst_g(self, new_gData):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_fst_g()
        wd.find_element_by_name("edit").click()
        self.fill_gform(new_gData)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        return len(wd.find_elements_by_name("selected[]"))