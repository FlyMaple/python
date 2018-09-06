# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                               Tuple                               #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 不能夠被改變

tuple_1 = (1, 1.23, 3.14j, 'String', [2, 3])
tuple_2 = ('A', 'B')
print(type(tuple_1))  # <class 'tuple'>

print(tuple_1[0:])
print(tuple_1[-3:-2])
print(tuple_1[2:3])
print(tuple_1 + tuple_2)
print(tuple_1 * 2)

# tuple_1[0] = 2

print(type(()))  # <class 'tuple'>
print(type((1)))  # <class 'int'>
print(type((12,)))  # <class 'tuple'>
t = 1, 2, "3", 4, 5
print(type(t))


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                      Function with Tuple                          #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
print("===========")
def func1(*args):
    print(type(args))
    print(args)
    return args

ret = func1(1, 2, 3, 4, 5)
print(type(ret))
print(ret)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                            常用函數                                #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# len、max、min、tuple