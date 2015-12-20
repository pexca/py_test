from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self): # representation, выводит на консоль заранее определённое представление объкта вместо его адреса
        return '%s:%s' % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id: return int(self.id)  # type str
        else: return maxsize  # максимальная целочисленная константа(индексация списка)




