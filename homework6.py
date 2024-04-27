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