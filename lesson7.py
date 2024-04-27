# def my1():
#     x = ['Jordan','Pasha','Pavel']
#     if 'Jordan' in x:
#         print(x)
#     else:
#         pass
# my1()

# import requests
# link = 'https://icanhazip.com/'
# print(requests.get(link).text)

import requests


url = 'https://httpbin.org/post'
data = {
        'custname': 'Elon Musk',
        'custtel': '+998999999990',
        'custemail': 'real-elon@mail.com',
        'size': 'small',
        'topping': 'cheese',
        'delivery': '12:00',
        'comments': 'hahahahha'}
print(requests.post(url,data=data))
