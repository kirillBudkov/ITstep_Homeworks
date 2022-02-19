# # task 1
# _list=["a",1,4,6,7,'g','2']
# count=0
# for i in _list:
#     count+=1
# print(count)

#
# # #task 2
# goods=['apple', "meet", 'butter', 'juice','milk']
# while True:
#     if len(goods)!=0:
#         check=input("enter your product: ")
#         if check in goods:
#             print(f'Вы купили {check}')
#             goods.remove(check)
#         else:
#             print(f'{check} в списке нет')
#     else:
#         print('все продукты куплены')
#         break

#task 2_up
# goods=['apple', "meet", 'butter', 'juice','milk']
# backet=[]
# while len(goods)>0:
#         check=input("enter your product: ")
#         if check in goods:
#             print(f'Вы купили {check}')
#             goods.remove(check)
#             backet.append(check)
#         elif check in backet:
#             print(f'{check} уже купили')
#         else:
#             print(f'{check} в списке нет')
# else:
#     print('все продукты куплены')

