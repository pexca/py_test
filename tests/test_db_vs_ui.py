from model.group import Group
from timeit import timeit

# compare db group list versus ui group list


def test_group_list(app, db):  # access db and ui via app and db fixtures
    print(timeit(lambda: app.group.get_gr_list(), number=1)) # по умолчанию timeit вызывает функцию миллион раз, поэтому number=1

    def clean(group):
        return Group(id=group.id, name=group.name.strip())  # remove extra spaces to match db and ui data
    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))  # obtain list with spaces removed
    assert False # sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
