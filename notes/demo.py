# Number
# int、long(廢棄)、float、complex
score = 100
print(type(score))

height = 123.78
print(type(height))

pi = 3.14j
print(type(pi))

# String
name = "我是 Skye，來自新竹，是個前端工程師~"
print(type(name))
print(name)
print(name[0])
print(name[0:2])
print(name * 3)
print(name + " GO")

# List 複數、有順序的集合、長度可變動
list_1 = [1, 2.3, 4j, "String"]
list_2 = ["Skye", "Annie", "Thwu"]
print(type(list_1))
print(len(list_1))
print(list_1 + list_2)
print(list_1 * 2)
for i in list_1:
    print(i)

# Tuple

# Dictionary


# **
print(2 ** 10)

# & 二進制 AND 計算
# | 二進制 OR 計算
# ^ 二進制 XOR 計算
# ~ 二進制 NOT 計算

# for
for i in range(4):
    print(i)

# while
begin = 10
end = 100
step = 10
while (begin < end):
    print(begin)
    begin = begin + step

# if else
score = 60
if score >= 60:
    print("及格")   
else:
    print("不及格")

# if elif lse
score = -1
if score >=0 and score < 60:
    print("不及格")
elif score >= 60 and score <=79:
    print("普通")
elif score >=80 and score <=99:
    print("不錯")
elif score == 100:
    print("滿分")
else:
    print("啥")

# function
list_1 = [1, 2, 3, 4, 5]
def func1(_list):
    for i in _list:
        print(i)
    return

# TODO: sort function
list_1 = [23, 50, 1, 25, 56, 98, 12, 23, 64, 14, 78, 60]

# file
file = open('note.txt', 'w+')
file.write('hi')
file.close()

# try except
try:
    r = request.get('12345')
except Exception:
    print('Exception!')

# assert 條件必須為這樣
year = 2018
assert year >= 2018, "Assert abort!"
print('After assert')

# class
class MyClz:
    def __init__(self, name):
        self.name = name

print(type(MyClz))
print(MyClz)


class Person:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def jump(self):
        print(self)
        print('跳')


class Driver:
    def drive(self):
        print(self)
        print('開車')