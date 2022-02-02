# # task 1
# inp1 = int(input('enter start of range: '))
# inp2 = int(input('enter end of range: '))
# evensum = 0
# oddsum = 0
# tonine = 0
# totalsum = 0
# count=0
# for i in range(inp1, inp2 + 1):
#     count+=1
#     totalsum+=i
#     if i % 2 == 0:
#         evensum += i
#     elif i % 2 != 0:
#         oddsum += i
#     if i % 9 == 0:
#         tonine += 1
# print('sum even is: ', evensum)
# print('sum odd is: ', oddsum)
# print('number multiply of 9 is: ', tonine)
# print('average is: ', totalsum/count)



# length= int(input('enter line length: '))
# symb=input('enter symbol: ')
# i=1
# while i <= length:
#     print(symb)
#     i += 1

# task3
# while True:
#     digit = float(input('enter digit: '))
#     if digit == 7:
#         print('Goodbye')
#         break
#     else:
#         if digit > 0:
#             print('Number is positive')
#         elif digit < 0:
#             print('Number is negative')
#         else:
#             print('Number is equal to zero')

# task 4
# res = 0
# i = 0
# while True:
#     digit = int(input('enter digit: '))
#     if digit == 7:
#         print('Goodbye')
#         break
#     res += digit
#     if i > 0:
#         print('sum is: ', res)
#         if digit < _min:
#             _min = digit
#             print('min is ', _min)
#         else:
#             print('min is: ', _min)
#         if digit > _max:
#             _max = digit
#             print('max is: ', _max)
#         else:
#             print('max is: ', _max)
#         continue
#     i += 1
#     _min = digit
#     _max = digit
