#
#
# nums = [i for i in range(1,11)]
# chotnie = [num for num in nums if num %2==0]
# nechotnie = [num for num in nums if num %2!=0]
# print(chotnie,nechotnie)
#
#
# names = ['pavel','jordan','sasha']
# names2 = [name for name in names if 'o' in name]
# print(names2)
# my = ['2', '33', 'jordan', 'pavel']
# my2 = [i+'2' for i in my if 'a' in i]
# print(my2)
#
# my_list = [i for i in range(1,11,2)]
# print(my_list)

# names =['Pavel ','Sasha ', 'Jordan ','Pasha ']
# answer = [i[0] for i in names ]
# print(answer

# nums = [i for i in range(1,21)]
# chotnie = [num for num in nums if num %2==0]
#
# print(chotnie)

usernames = []
while True:
    
    user1 = input('Введите имя : ')


    if user1 in usernames:
        print('Это имя уже занято ! Выберите другое имя ')

    else:
        usernames.append(user1)
        print('Добавленно ')
        print(usernames)
