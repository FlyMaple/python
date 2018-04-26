# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                            數據類型轉換                            #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# int
print("==============")
print(int("1234", 10))  # 1234
print(int("1111", 2))  # 15
print(int("F", 16))  # A

# float
print("==============")
print(float("999"))  # 999.0
print(float(1234))

# complex
print("==============")
print(complex(3.14 + 123j))  # (3.14+123j)

# str
print("==============")
print(str(123456))  # 123456
print(str(123.456))  # 123.456
print(str([1, 2, 3]))  # [1, 2, 3]
print(str({"name": "skye"}))  # {'name': 'skye'}

# repr 可以和 str 做比較，搞不懂
print("==============")

# eval
print("==============")
o = eval("1+2+3")
print(o)  # 6

# tuple
print("==============")
print(tuple([1, 2, 3, 'aaaaaa']))  # (1, 2, 3, 'aaaaaa')
print(tuple('abcde'))  # ('a', 'b', 'c', 'd', 'e')

# list
print("==============")
print(list([1, 2, 3, 'aaaaaa']))  # [1, 2, 3, 'aaaaaa']
print(list('abcde'))  # ['a', 'b', 'c', 'd', 'e']

# set
print("==============")
print(set([1, 2, 3, 'aaaaaa', 1]))  # {1, 2, 3, 'aaaaaa'}
# {'d', 'e', 'a', '5', '2', 'c', 'b', '4', '3', '1'}
print(set('abcde12345abcde'))

# dict
print("==============")
print(dict({"name": "skye"}))  # {'name': 'skye'}
print(dict([["name", "skye"]]))  # {'name': 'skye'}
print(dict([("name", "skye")]))  # {'name': 'skye'}

# frozenset 凍結
print("==============")
frozenset({"name": "skye", "age": 18})  # frozenset({'name', 'age'})
frozenset({"name", "age"})  # frozenset({'name', 'age'})
frozenset('asd')  # frozenset({'s', 'a', 'd'})
frozenset([1, 2, 3, 4, 5])  # frozenset({1, 2, 3, 4, 5})
frozenset((1, 2, 3, 4, 5))  # frozenset({1, 2, 3, 4, 5})

# chr
print("==============")
print(chr(97))  # a
print(chr(65))  # A

# ord
print("==============")
print(ord('a'))  # 97
print(ord('A'))  # 65

# hex
print("==============")
print(hex(0))  # 0x0
print(hex(10))  # 0xa
print(hex(15))  # 0xf

# oct
print("==============")
print(oct(0))  # 0o0
print(oct(7))  # 0o7
print(oct(8))  # 010
