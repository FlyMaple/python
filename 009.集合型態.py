# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                               Sets                                #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 無順序，不重複

print(type(set()))  # <class 'set'>
print(type({1, 2, 3, 4, 5}))  # <class 'set'>

set_1 = {'Skye', 'Tina', 'Thwu', 'Skye', 'Thwu'}
print("===============")
print(set_1)  # {'Skye', 'Tina', 'Thwu'}


print("===============")
name = 'Skye'
if name in set_1:
    print('在集合中')
else:
    print('不在集合中')


print("===============")
set_1 = {'Skye', 'Tina', 'Thwu'}
set_2 = {'Tina', 'Kai'}
print(set_1 - set_2)  # {'Skye', 'Thwu'} # 差急
print(set_1 | set_2)  # {'Skye', 'Tina', 'Thwu', 'Kai'} # 聯集
print(set_1 & set_2)  # {'Tina'} # 交集
print(set_1 ^ set_2)  # {'Skye', 'Thwu', 'Kai'} # 不同時出現的


print("===============")
print(set('python'))  # {'o', 't', 'h', 'n', 'y', 'p'}
