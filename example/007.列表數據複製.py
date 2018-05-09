# 提問：將一個列表的數據複製到另一個列表中。

list_1 = [1, 1, 1]
list_2 = list_1.copy()
list_3 = list_1.copy()

from copy import copy
list_4 = copy(list_1)
list_5 = copy(list_1)

list_6 = list_1[:]
list_7 = list_1[0:]

print("list_1 id: {}".format(id(list_1)))
print("list_2 id: {}".format(id(list_2)))
print("list_3 id: {}".format(id(list_3)))
print("list_4 id: {}".format(id(list_4)))
print("list_5 id: {}".format(id(list_5)))
print("list_6 id: {}".format(id(list_6)))
print("list_7 id: {}".format(id(list_7)))

