# 簡述：9*9乘法口訣表。
# 要求：逐項單位輸出。例如1的一行，2的一行，以此類推。

for i in range(1, 10):
    for j in range(1, 10):
        if j < 9:
            print("{} x {} = {}".format(i, j, i*j), end=" ")
        else:
            print("{} x {} = {}".format(i, j, i*j))