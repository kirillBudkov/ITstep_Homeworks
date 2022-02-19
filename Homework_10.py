# 1) Есть список блюд. Запросить блюдо через input, и удалить его из списка. В случае ошибки - обработать, и вывести на экран, что такого блюда нет.
#
# 2) Попробовать удалить элемент из кортежа. Обработать ошибку.
#
# 3) Вызвать несуществующий метод списка, обработать ошибку.
#
# 4) У вас есть строка. Заменить все символы "а" на "@"


# task 1
# meals=['apple', "meet", 'butter', 'juice','milk']
# try:
#     meal=input("enter meal: ")
#     meals.remove(meal)
# except ValueError:
#     print('Out of menu')
# except BaseException:
#     print('Error: something happened')

#task 2

# _tuple = ('apple', "meet", 'butter', 'juice','milk')
# try:
#     _tuple.remove('apple')
# except:
#     print("it's a tuple Bro!")
#task 3
# _list = ['apple', "meet", 'butter', 'juice','milk']
# try:
#     _list.makemecoffe('coffe')
# except AttributeError as error:
#      print(error)

#task 4
# _str='minam veniam, quis nostrad exercitation ullamco laboris'
# _strNew=_str.replace('a','@')
# print(_strNew)