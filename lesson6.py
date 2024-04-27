#Словари


# x = {'name':'Pasha','job':'TGbot creator'}
# print(x['name'])
# print(x['job'])
# print(x['name'],x['job'])


# data = {'name':['Jordan','Pavel'],
#         'age':(12,21),
#         'job':'programers'}
# print(data['name'][0],data['job'][-1])

# instructor = {'name':'Jordan','age':21,'job':'programmer'}
# if 21 in instructor.values():
#     print('Да есть ')
# else:
#     print('Не понимаю о чем вы ')
#
# print(instructor.values())
# print(instructor.keys())
# print(instructor.items())

#Добавление новых ключ значений
#
# users = {}
# users['name'] = 'Jordan'
# print(users)
# print(users['name'])


# my_dict = {'name':'Jordan'}
# my_dict['name'] = 'Pasha'
# print(my_dict)

# user = ['post','likes','comments','followers','following','saves','stories']
# user1 = {}.fromkeys(user,0)
# print(user1)

# instructor = dict(name='Jordan', age=21, job='programmer')
# for i in instructor.keys():
#     print(i)
# for e in instructor.values():
#     print(e)
# for k,v  in instructor.items():
#     print(k,v)


all_products = {'Весь склад ':{}}
korzina = {}
while True:
    admin = input('Что вы хотите сделать? ')
    if admin.lower()=='добавить':
        product_name = input('Введите название продукта: ')
        product_count = int(input('Введите колличество: '))
        all_products['Весь склад '][product_name]=product_count
        print('Продукт добавлен!')
    elif admin.lower()=='продукты':
        print(all_products)
    elif admin.lower()== 'купить':
        print(all_products)
        user_product = input('Какой товар желаете купить? ')
        if user_product in all_products['Весь склад ']:
            user_count = int(input('Сколько желаете? '))
            all_products['Весь склад '][user_product] -= user_count

            korzina[user_product] = user_count
            print('Ваш заказ добавлен в корзину!')
        else:
            print('Такого продукта нет!')
    elif admin.lower() == 'корзина':
        print(korzina)

