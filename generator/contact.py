from model.contact import *
import random
import string  # константы, хранящие списки символов
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
    # n stands for number of generated contacts, f stands for file to write it to
except getopt.GetoptError as err:
        # print help information and exit:
    print(str(err))  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

n = 4
f = 'data/contacts.json'
# генератор управляется опциями -n и -f
for o, a in opts:
    if o == '-n':  # contacts quantity
        n = int(a)
    elif o == '-f':  # name of file
        f = a


def randstring(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+string.punctuation+' '*5  # add 5 spaces
    return prefix+''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    # генерирует строчку случайной длины, не прев.мах

#  add empty contact once, add random contact 4 times
test_data = [Contact(firstname="", lastname="", email="")] + [
    Contact(firstname=randstring('fname', 10), lastname=randstring('lname', 10), email=randstring('email', 10))
    for i in range(4)
]

# склеивается путь к генератору+переход на две директории вверх+строка из переменной f
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(test_data))

'''
with open(file, 'w') as out:
    out.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))

.dumps превращает текст в строку в формате json, но json не умеет преобразовывать объект типа
    Group в строку в формате json, поэтому для всех подобных случаев определён параметр default,
    в котором указана функция, которую json.dumps применит к данным прежде, чем попытается преобразовать их в json,
    __dict__ - стандартное свойство объекта, в котором хранятся данные о его конструкторе.'''

'''
#  генерирует комбинации тестовых данных
test_data = [
    Contact(firstname=fname, lastname=lname, email=email)
    for fname in ['', randstring('fname', 10)]
    for lname in ['', randstring('lname', 10)]
    for email in ['', randstring('email', 10)]
]
'''
