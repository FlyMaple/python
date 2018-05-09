# 整數順序排列問題簡述：任意三個整數類型，x、y、z 
# 提問：要求把這三個數，按照由小到大的順序輸出

_list = []
_list.append(int(input("a = "), 10))
_list.append(int(input("b = "), 10))
_list.append(int(input("c = "), 10))
_list.sort()

print("由小到大: ", end="")
for i in _list:
    print("{}".format(i), end=", ")

print("")

_list.sort(key = None, reverse = True)
print("由大到小: ", end="")
for i in _list:
    print("{}".format(i), end=", ")