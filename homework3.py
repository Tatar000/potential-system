contact = ['Roberto', 'Georgio', 'Ralph']

choice = input('1-Добавить\n2-Изменить\n3-Удалить\nВаш выбор: ')

if choice == '1':
    new_name = input('Введите имя: ')
    contact.append(new_name)
    print(contact)

elif choice == '2':
    print(contact)
    edit_name = input('Напишите имя для изменния: ')
    newname = input('Введите новое имя: ')

    # Сохронили индекс имени -->
    index_name = contact.index(edit_name)

    # Удаление по индексу -->
    contact.pop(index_name)

    # Мы вставляем новое имя
    # на место старого используя его индекс -->
    # list.insert(index, new_name))
    contact.insert(index_name, newname)

    print(contact)
elif choice == '3':
    print(contact)
    udalenie = input('Viberite kogo udalit ')
    contact.remove(udalenie)
    print(contact)
else:
    print(contact)
