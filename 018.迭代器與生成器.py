# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                              Iterator                             #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
_list = ['A', 'B', 'C']

it = iter(_list)  # <list_iterator object at 0x000002721A9A1F98>
print(type(it))  # <class 'list_iterator'>

print(next(it)) # A
print(next(it)) # B
print(next(it)) # C
# print(next(it)) # StopIteration

print('-------------------')

for i in ['A', 'B', 'C']:
    print(i)

print('-------------------')

for i in iter(['A', 'B', 'C']):
    print(i);

print('-------------------')

_list = ['A', 'B', 'C']
it = iter(_list)

try:
    while True:
        print(next(it))
    else:
        print('iter done.')
except StopIteration:
    print('try except.')
    print(i);

print('-------------------')

_list = ['A', 'B', 'C']
it = iter(_list)

while True:
    try:
        print(next(it))
    except StopIteration:
        print('try except done.')
        break


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                        generator / yield                          #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# generator 用來產生 iterator
# 遇到 yield 暫停，並保留當前訊息
# 沒有理解