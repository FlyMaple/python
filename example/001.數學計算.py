# 簡述：這裡有四個數字，分別是：1、2、3、4
# 提問：能組成多少個互不相同且無重複數字的三位數？各是多少？
# http://www.iplaypy.com/python-100/7089.html

_list = [1, 2, 3, 4]
total_list = []

for i in _list:
    for j in _list:
        if j != i:
            for k in _list:
                if k != j:
                    s = "{0:^3d}{1:^3d}{2:^3d}".format(i, j, k)
                    total_list.append(s)


def result():
    for i in total_list:
        print(i)

    print("------------")
    print("共 {} 筆.".format(len(total_list)))

# result()


def result2():
    for i in iter(set(total_list)):
        print(i)

    print("------------")
    print("共 {} 筆.".format(len(total_list)))

# result2()