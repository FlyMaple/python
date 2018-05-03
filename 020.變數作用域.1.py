# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                             變數作用域                             #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# L (Local) 區域
# E (Enclosing) 必包函數外的函數中
# G (Global) 全域
# B (Built-in) 內建域

init = True  # 全域


def func1():
    print(init)
    func1_var = 'func1_var'  # 區域

    def func1_1():
        print(init)
        print(func1_var)
        func1_1_var = 'func1_1_var'  # 區域

    func1_1()


print(init)
func1()

print('-----------------')

# print(msg)

if True:
    msg = 'Message'

print(msg)

while True:
    mess = 'Mess'
    break

print(mess)

print('-----------------')


def func4():
    init = 123
    # global init
    # init = 123
    print(init)


func4()
print(init)

print('-----------------')


def func5():
    outer = 'outer'

    def func5_5():
        inter = 'inter'
        outer = 'inter_outer'
        # nonlocal outer
        # outer = 'yoyoyoyoyo'
        print(outer)
        print(inter)

    print(outer)
    func5_5()
    print(outer)


func5()

print('-----------------')

# 預設值要放最後
# SyntaxError: non-default argument follows default argument
# def func6(name=None, age):
#     print(name)
#     print(age)

# func6()

print('-----------------')


def func7(**args):
    print(args)


func7(name='skye', age=18, skill=[])


print('-----------------')

func8 = lambda x=10, y=20: x**2 + y**2
print(func8())
print(func8(1, 2))

print('-----------------')

func9 = lambda name, age: name + age
print(func9('skye', '18'))
print(func9(age='22', name='kai'))

print('-----------------')
