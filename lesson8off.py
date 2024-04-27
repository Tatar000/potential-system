# a = lambda  x:x**2
# print(a(10))
#
# b = lambda y, u:y+u
# print(b(2,3))
# while True:
#     c = int(input('Введите сторону c'))
#     y = int(input('Введите значение y'))
#     r = lambda  y, c: (y + c ) * 2
#     print(r(y,c))

# while True:
#
#     y = int(input('Введите значение y'))
#     r = lambda  y: y * 4
#     print(r(y))

# def spam(a,b,c=7):
#     return a+b+c
# print(spam(3,5,10))

# def spam(a,b):
#     return (a+b)**2
# print(spam(3,5))

# all_products = {'Склад':{'name':'Хлеб','количество':34}}
# def get_products(a):
#     print(all_products['Склад'][a])
# get_products('name')


# def spam1(*args):
#     return args
# print(spam1(1,2,3,'Hello'))

# def spam(*blabla):
#     for i in blabla:
#         print(i)
# spam(1,2,3,'Hi',15.2)

# def spam1(**kwargs):
#     return kwargs
# print(spam1(name='my1',age=23))

clients = {}
opened_rooms = [ i for i in range(1, 21)]
closed_rooms = []


def register(name,room):
    clients[name]=room
    opened_rooms.remove(room)
    closed_rooms.append(room)
    return 'Клиент успешно зарегестрировался'


def check_out(name):
    closed_rooms.remove(clients[name])
    opened_rooms.append(clients[name])
    clients.pop(name)
    return 'Клиент успешно выселен'
def show_rooms():
    return closed_rooms
while True:
    choise = input('Что хотите сделать? ')
    if choise.lower()=='зарегестрировать':
        cl_name =input('Имя клиента: ')
        print(opened_rooms)
        cl_room = input('Номер клиента')
        if cl_room.isnumeric():
            register(cl_name,int(cl_room))
        else:
            print('Ошибка! ')
    elif choise.lower()=='выселить':
        if clients:
            cl_name = input('Имя клиента: ')
            if cl_name in clients:
                check_out(cl_name)
            else:
                print('Такого клиента нет! ')
        else:
            print('Клиентов пока нет! ')
    elif choise.lower()=='комнаты':
        print('Занятые номера:\n',show_rooms())
    else:
        print('Ошибка')