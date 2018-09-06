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


print("=============")
o = {"name": "skye", "age": 18, "skill": [], "height": 174.5}
print(o)
for c in o:
    print("key: ", c, ", value: ", o[c], sep="")

print("=============")
o = {"name": "skye", "age": 18, "skill": [], "height": 174.5}
print(o)
for k,v in o.items():
    print("key:", k, end=", ")
    print("value:", v)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                            常用函數                                #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    
# clear、copy、fromkeys、get、in、items、keys、values、pop、popitem