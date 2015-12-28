

class Contact:

    def __init__(self, firstname=None, lastname=None, email=None, id=None,all_phnums_from_hp=None,
                 wphone=None, hphone=None, sphone=None, mphone=None, address=None, emails=None,
                 email2=None, email3=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.id = id
        self.wphone = wphone
        self.hphone = hphone
        self.sphone = sphone
        self.mphone = mphone
        self.all_phnums_from_hp = all_phnums_from_hp
        self.address = address
        self.emails = emails
        self.email2 = email2
        self.email3 = email3

    def __repr__(self):
        return '%s:%s' % (self.id, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname


