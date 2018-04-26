# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                              String                               #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
message = \
"""Line1
Line2"""
print("======")
print(message)
print("======")

message = "a\\nb\\nc"
print("======")
print(message)
print("======")

message = "This" " " "is" " " "Python."
print("======")
print(message)
print("======")

message = "Message"
print("======")
print(message + message)
print("======")

message = "Message"
print("======")
print(message * 3)
print("======")

str = "A1B2C3D4E5F6G7"
# A
print(str[0])

# A1
print(str[0:2])

# A1B2C3D4E5F6
print(str[0:-2])

# D4E5
print(str[6:10])

# B2C3D4E5F6G7
print(str[2:])


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                            Translation                            #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
print("*********")
print("\r\n\t")
print("*********")
# print(r"\r\n\t")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                            Format                                 #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
name = 'skye'
print('1234 %s 56 %s 78 %s 90 %d %s' % ('A', 'B', [name, name], 999, ('asd', 'dsa')))

# 符號   描述
# %c	 格式化字符及其ASCII码
# %s	 格式化字符串
# %d	 格式化整数
# %u	 格式化无符号整型
# %o	 格式化无符号八进制数
# %x	 格式化无符号十六进制数
# %X	 格式化无符号十六进制数（大写）
# %f	 格式化浮点数字，可指定小数点后的精度
# %e	 用科学计数法格式化浮点数
# %E	 作用同%e，用科学计数法格式化浮点数
# %g	 %f和%e的简写
# %G	 %f 和 %E 的简写
# %p	 用十六进制数格式化变量的地址

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                            常用函數                                #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#太多啦