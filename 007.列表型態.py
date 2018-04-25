# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                                List                               #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

list_1 = [1024, 1.23, 3.14j, 'String']
list_2 = [[1, 2, 3], 4, 5]

print(type(list_1)) # <class 'list'>
print(list_1[0]) # 1024
print(list_1[-1]) # String
print(list_1[1: 3]) # [1.23, 3.14j]
print(list_1[2:]) # [3.14j, 'String']
print(list_1 + list_2) # [1024, 1.23, 3.14j, 'String', [1, 2, 3], 4, 5]
print(list_1 * 2) # [1024, 1.23, 3.14j, 'String', 1024, 1.23, 3.14j, 'String']

list_1[0] = [1, 2]
print(list_1)

list_1[1:3] = ['A', 'B']
print(list_1)

list_1[0:1] = [1, 2]
print(list_1)

list_1[0:] = []
print(list_1);