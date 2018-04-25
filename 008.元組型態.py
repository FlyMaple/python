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
