# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                             Dictionary                            #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 無順序 key:value mapping

print(type({}))  # <class 'dict'>


print("=============")
obj = {}
obj["name"] = "Skye"
# obj.age = 18
obj["age"] = 18
obj[100] = 100
obj["100"] = "100"
print(obj)
print(obj.keys())  # dict_keys(['name', 'age', 100, '100'])
print(obj.values())  # dict_values(['Skye', 18, 100, '100'])
print(type(obj.keys()))  # <class 'dict_keys'>
print(type(obj.values()))  # <class 'dict_values'>

print("=============")
print(dict([["name", "Skye"], ["age", 18]]))  # {'name': 'Skye', 'age': 18}
print(dict([["name", "Skye"], ("age", 18)]))  # {'name': 'Skye', 'age': 18}
