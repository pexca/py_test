import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)  # init db connection
        self.connection.autocommit = True  # drop cache after each request completion

    def get_group_list(self):  # this method loads groups list directly from db
        lst = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
            for row in cursor:  # курсор - итерируемый объект, где каждая из строк представляет собой кортеж
                (id, name, header, footer) = row
                lst.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return lst

    def demolish(self):
        self.connection.close()  # соединение с БД сохраняется открытым в течение существования фикстуры


# адрес БД, сервер с БД, название БД, логин и пароль для доступа к ней - в конфигурационном файле target.json

    def get_contact_list(self):  # this method loads contacts list directly from db
        lst = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                lst.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return lst

