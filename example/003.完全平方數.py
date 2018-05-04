# 簡述：一個整數，它加上100和加上268後都是一個完全平方數

# 提問：請問該數是多少？
import math

for i in range(1000):
    if (math.sqrt(i + 100) % 1 == 0.0) and (math.sqrt(i + 268) % 1 == 0.0):
        print(i)
        break
    
