# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                              Number                               #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Number(數字)
# int、float、bool、complex


def _number():
    print(True == 1)
    print(False == 0)

    print("===============")
    print(int)
    print(float)
    print(bool)
    print(complex)
    print(isinstance(1024, int))
    print(isinstance(3.14, float))
    print(isinstance(3.14j, complex))
    print(isinstance(True, (int, bool)))

    print("===============")
    print(2 ** 10)
    print(17 / 3)
    print(17 // 3)
    print(17 % 3)

# _number()


# String(字串)

# List(列表)

# Tuple(元組)

# Sets(集合)

# Dictionary(字典)

# 不可變 Number、String、Tuple、Sets
# 可變 List、Dictionary
# 有順序 String、List、Tuple
