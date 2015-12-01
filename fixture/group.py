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
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_gp()

    def open_gp(self):
        wd = self.app.wd
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def del_fst_group(self):
        wd = self.app.wd
        self.open_gp()
        #select first group
        #submit group deletion
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        wd.find_element_by_link_text("group page").click()

    def rename(self):
        wd = self.app.wd
        self.open_gp()
        if not wd.find_element_by_name("selected[]").is_selected():
            wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("qwerty/renamed")
        wd.find_element_by_css_selector("#content > form").click()
        wd.find_element_by_css_selector("#content > form").click()
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("group page").click()