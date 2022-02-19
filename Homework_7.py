_str = input("enter string: ")

# task 1
# print(_str[::-1])

# task 2
letter = 0
digit = 0
for i in _str:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        digit += 1
print(f"letters: {letter}, digits: {digit}")

# task 3
search = input("enter item: ")
print(_str.count(search))

# task 4
search = input("enter word: ")
count = 0
_list = _str.split()
for i in _list:
    if i == search:
        count += 1
if not count:
    print("not found")
else:
    print(count)

# task 5
search = input("enter word: ")
replace = input("enter word to replace: ")
_list = _str.split()
for i in _list:
    if i == search:
        pos = _list.index(i)
        _list.remove(i)
        _list.insert(pos, replace)
print(" ".join(_list))
