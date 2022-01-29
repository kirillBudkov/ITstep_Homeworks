# task 1
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day = int(input("choose day: "))
if 0 < day <= 7:
    print(week[day - 1])
else:
    print('select from 1 to 7')

# task 2
year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
        'December']
month = int(input("choose month: "))
if 0 < month <= 12:
    print(year[month - 1])
else:
    print('select from 1 to 12')

# task3
digit = float(input('enter digit: '))
if digit > 0:
    print('Number is positive')
elif digit < 0:
    print('Number is negative')
else:
    print('Number is equal to zero')

# task4
inp1=float(input('enter value1: '))
inp2=float(input('enter value2: '))
if inp1>inp2:
    print(inp1,inp2)
elif inp1<inp2:
    print(inp2,inp1)
else:
    print("equal")

