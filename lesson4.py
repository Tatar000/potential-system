names = []
number = []
service = []
print(names,number,service)
choice = input('1-Добавить имя\n2-Добавить номер\n3-Выбрать услугу\nВаш выбор: ')

while True:
    if choice == '1':
        new_name = input('Введите имя: ')
        names.append(new_name)
        print(names)
        choice = input('1-Добавить имя\n2-Добавить номер\n3-Выбрать услугу\nВаш выбор: ')
    elif choice == '2':
        new_number = input('Введите номер: ')
        number.append(new_number)
        print(number)
        choice = input('1-Добавить имя\n2-Добавить номер\n3-Выбрать услугу\nВаш выбор: ')
    elif choice == '3':
        new_service = input('Выбрите услугу: ')
        service.append(new_service)
        print(service)
        choice = input('1-Добавить имя\n2-Добавить номер\n3-Выбрать услугу\nВаш выбор: ')