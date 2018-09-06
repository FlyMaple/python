# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                          序列 / 反序列                             #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import pickle, pprint
obj = {
    "name": "AP",
    "url": "/ap",
    "orgSiteCheck": True,
    "log": [1, 2],
    "_t": (1, 2, 3),
    "_dict": {"name": u"skye國"},
    "n": None
}
_list = ["A", "B"]
_list.append(_list)

# print(obj)
# print(_list)

# print(dir(pickle))

# f = open("data.pkl", "wb")

# pickle.dump(obj, f)

# pickle.dump(_list, f)

# f.close()

##################################

f = open("data.pkl", "rb")

data1 = pickle.load(f)

pprint.pprint(data1)

data2 = pickle.load(f)

pprint.pprint(data2)

f.close()