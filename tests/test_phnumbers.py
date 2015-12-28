import re
from random import randrange

# тест сравнивает данные о телефонах контактов, отображаемых на главной странице с телефонами на странице
# редактирования, функция 'clear' при этом очищает полученную запись от лишних символов:

'''
def test_phnumbers_on_hp(app):
    cont_from_hp = app.contact.get_conts_lst()[0]  # obtain first contact from homepage
    cont_from_edit_page = app.contact.get_cont_info_from_edit_page(0)
    assert cont_from_hp.all_phnums_from_hp == merge_phnums_like_on_hp(cont_from_edit_page)
'''


def test_the_rest(app):
    cont_from_hp = app.contact.get_conts_lst()
    idx = randrange(len(cont_from_hp))
    contact = app.contact.get_conts_lst()[idx]
    cont_from_edit_page = app.contact.get_cont_info_from_edit_page(idx)
    assert contact.all_phnums_from_hp == merge_phnums_like_on_hp(cont_from_edit_page)
    assert contact.firstname == cont_from_edit_page.firstname
    assert contact.lastname == cont_from_edit_page.lastname
    assert contact.address == cont_from_edit_page.address
    assert contact.emails == merge_emails_like_on_hp(cont_from_edit_page)


def clear(s):
    return re.sub('[() -]', '', s)  # replace braces, space and/or hyphen with empty space


def merge_emails_like_on_hp(contact):
    return '\n'.join(filter(lambda x: x != '',
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))


def merge_phnums_like_on_hp(contact):
    return '\n'.join(filter(lambda x: x != '',  # применяем filter, чтобы избавиться от пустых строк
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.hphone, contact.mphone, contact.wphone,
                                                                 contact.sphone]))))
    # применяем map clear x ко всем элементам списка, чтобы очистить строки от лишних символов

'''
def test_phnumbers_on_cont_viewpage(app):
    cont_from_view_page = app.contact.get_cont_from_viewpage(0)
    cont_from_edit_page = app.contact.get_cont_info_from_edit_page(0)
    assert cont_from_view_page.hphone == cont_from_edit_page.hphone
    assert cont_from_view_page.mphone == cont_from_edit_page.mphone
    assert cont_from_view_page.wphone == cont_from_edit_page.wphone
    assert cont_from_view_page.sphone == cont_from_edit_page.sphone

def test_phnumbers_on_hp(app):
    cont_from_hp = app.contact.get_conts_lst()[0]  # obtain first contact from homepage
    cont_from_edit_page = app.contact.get_cont_info_from_edit_page(0)
    assert cont_from_hp.hphone == clear(cont_from_edit_page.hphone)
    assert cont_from_hp.mphone == clear(cont_from_edit_page.mphone)
    assert cont_from_hp.wphone == clear(cont_from_edit_page.wphone)
    assert cont_from_hp.sphone == clear(cont_from_edit_page.sphone)
'''
