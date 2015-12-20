from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.id = id

    def __repr__(self):
        return '%s:%s' % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname


