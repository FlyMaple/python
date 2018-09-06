# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                                                                   #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
count = 100

while count >= 0:
    print(count)
    count -= 1

print('-----------------')

begin = 1
total = 0
while begin <= 100:
    total += begin
    begin += 1
else:
    print(total)

print('-----------------')

for i in ['A', 'B', 'C']:
    print(i)

print('-----------------')

for i in range(10):
    print(i)

print('-----------------')

for i in range(0, 10, 2):
    print(i)

print('-----------------')

_list = ['A', 'B', 'C']

for i in range(len(_list)):
    print(_list[i])

for i, j in enumerate(_list):
    print('%d => %s' % (i, j))