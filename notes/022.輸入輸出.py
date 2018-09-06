# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                             Input                                 #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# print('{}'.format(input('Input:')))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                             Output                                #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# print('%s %s' % ('kai', 'thwu'))
# print('{}'.foramt())
# print('{0}'.foramt())
# print('{name}'.foramt())
# print('{0[name]:s}'.foramt({}))
# print('{name:s}'.foramt(**{}))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                             File                                  #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
f = open('note.txt', 'r+')

# f.write('1')
# f.write('2')
# f.write('3')

# print(f.readline())
# print(f.readline())
# print(f.readline())

for line in f.readlines():
    print(line, end='')

f.close()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                          序列 / 反序列                             #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #