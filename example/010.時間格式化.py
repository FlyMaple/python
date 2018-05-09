# 暫停一秒time.sleep()輸出；並格式化當前時間
# '2018-05-08 14:55:38 Tuesday'
import time
print(time.strftime("%Y-%m-%d %H:%M:%S %A",time.localtime()))
time.sleep(1)
print(time.strftime("%Y-%m-%d %H:%M:%S %A",time.localtime()))
time.sleep(1)
print(time.strftime("%Y-%m-%d %H:%M:%S %A",time.localtime()))
time.sleep(1)
print(time.strftime("%Y-%m-%d %H:%M:%S %A",time.localtime()))