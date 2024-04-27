# class Apple:
#     name = 'Iphone'
#
# phone1 = Apple()
# print(phone1.name)

# class Boy:
#     def __init__(self, nation, color, age):
#         self.namtion = nation
#         self.color = color
#         self.age = age
#
# negr = Boy('cigan','very Black',20)
#
# print(vars(negr))

# class Comment:
#     def __init__(self, username, text, likes = 0 ):
#         self.username = username
#         self.text = text
#         self.likes = likes
#
#     def change_text(self,new_text):
#         self.text = new_text
#
# user1 = Comment('Roman','sosu za kolbasu, kachestvenno!!!' , 9999999)
# print(vars(user1))
# user1.change_text('Dau ne po dnyam a po chasam')
# print(user1.text)


class BankAccount:
    def __init__(self, name, balance = 0.0 ):
        self.name = name
        self.balance = balance


    def deposite(self, new_deposite):
        self.balance += new_deposite

    def cash(self, new_deposite):
        self.balance -= new_deposite

    def my_balance(self):
        print(self.balance)


user1 = BankAccount('Roman')
print(vars(user1))

