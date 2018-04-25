# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                           keyword module                          #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import keyword

print(keyword)

# <class 'module'>
print(type(keyword))

# keyword module 底下所有的屬性(property)和函數(function)
# ['iskeyword', 'kwlist']
print(keyword.__all__)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print(keyword.kwlist)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                             Comments                              #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
print("註解前")
'''
我是多行註解1
我是多行註解2
我是多行註解3
'''
print("註解中")
"""
我是多行註解4
我是多行註解5
我是多行註解6
"""
print("註解後")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                             Multi line                            #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
message = "Message1" + \
          "Message2" + \
          "Message3"
print(message)
