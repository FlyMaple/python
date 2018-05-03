# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                             Function                              #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 必要參數
# 關鍵字參數
# 默認參數
# 不定長度參數


def func1(name, age):
    print('Name: %s' % name)
    print('Age: %s' % age)

# TypeError: func1() missing 2 required positional arguments: 'name' and 'age'
# func1()


func1('Skye', 18)

print('----------------------')

func1(age=18, name='thwu')

print('----------------------')


def func2(name=None, age=None):
    print('Name: %s' % name)
    print('Age: %s' % age)


func2()

print('----------------------')


def func3(name=None, age=None, *argv):
    print('Name: %s' % name)
    print('Age: %s' % age)
    print('Args:', argv)


func3('kai', 18, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print('----------------------')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                              lambda                               #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def sum(a, b): return a + b


print(sum)  # <function <lambda> at 0x0000023FD6C000D0>
print(type(sum))  # <class 'function'>
print(sum(25, 75))