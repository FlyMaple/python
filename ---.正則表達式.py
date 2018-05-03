# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                              Regexp                               #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# match 從字串開投匹配
import re

# <_sre.SRE_Match object; span=(0, 3), match='www'>
print(re.match('www', 'www.gamer.com.tw'))

# (0, 3)
print(re.match('www', 'www.gamer.com.tw').span())
print(re.match('www', 'www.gamer.com.tw'))

# <class 'tuple'>
print(type(re.match('www', 'www.gamer.com.tw').span()))

# None
print(re.match('www', 'http://www.google.com.tw'))

# None
print(re.match('gamer', 'www.gamer.com.tw'))

print('---------------------------')

line = 'Cats are smarter than dogs'
print(line)
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
print(matchObj)
print(matchObj.group())  # Cats are smarter than dogs
print(matchObj.group(1))  # Cats
print(matchObj.group(2))  # smarter
print(matchObj.groups())  # ('Cats', 'smarter')

print('---------------------------')


# search 字串整段匹配
#
# <_sre.SRE_Match object; span=(0, 3), match='www'>
print(re.search('www', 'www.google.com.tw'))

# <_sre.SRE_Match object; span=(15, 17), match='tw'>
print(re.search('tw', 'www.google.com.tw'))

print('---------------------------')


# sub 替換
#
# [a:b:c:d:e:f:g:h:i:j]
line = '[a:b:c:d:e:f:g:h:i:j]'
print(line)

line = re.sub(r':', ' = ', line,)
# [a = b = c = d = e = f = g = h = i = j]
print(line)

line = re.sub(r' = ', ' || ', line, 3)
# [a || b || c || d = e = f = g = h = i = j]
print(line)

print('---------------------------')

line = "0912-345-678 # 這是一個電話號碼"

# 刪除註解
line = re.sub(' #.*', '', line)
print(line)
# 刪除非數字
line = re.sub('\D', '', line)
print(line)

print('---------------------------')


def func1(matched):
    print(matched)
    return str(int(matched.group(), 10) * 2)


line = 'A23G4HFD567'
print(re.sub('\d+', func1, line))  # A46G8HFD1134
print(re.sub('\d+', func1, line, 1))  # A46G4HFD567

print('---------------------------')


line = 'A23G4HFD567'
pattern = re.compile('\d+')

# None
print(pattern.match(line))
# <_sre.SRE_Match object; span=(4, 5), match='4'>
print(pattern.match(line, 4))

# <_sre.SRE_Match object; span=(1, 3), match='23'>
print(pattern.search(line))

# <_sre.SRE_Match object; span=(8, 11), match='567'>
print(pattern.search(line, 6))
print(pattern.search(line, 6).group())
print(pattern.search(line, 6).start())
print(pattern.search(line, 6).end())
print(pattern.search(line, 6).span())

print('---------------------------')


# findall
#
# 匹配多次
line = 'aa bb cc dd ee ff'
pattern = re.compile(r'(\w+) (\w+)')
matchObj = pattern.match(line)
print(matchObj.group(1))  # aa
print(matchObj.span(1))

print(pattern.findall(line))  # [('aa', 'bb'), ('cc', 'dd'), ('ee', 'ff')]
print(pattern.findall(line, 2)) # [('bb', 'cc'), ('dd', 'ee')]
print(pattern.findall(line, 2, 8)) # [('bb', 'cc')]

it = pattern.finditer(line)
print(it) # <callable_iterator object at 0x000001BFA4B25EF0>

for i in it:
    print(i)
    print(i.group())



print('---------------------------')

# split
#
# 分割字串並返回列表
line = 'aa, bb, cc, dd, ee'
print(re.split(r'(\W+)', line)) # ['aa', ', ', 'bb', ', ', 'cc', ', ', 'dd', ', ', 'ee']
print(re.split(r'\W+', line)) # ['aa', 'bb', 'cc', 'dd', 'ee']
print(re.split(r',\s+', line, 1)) # ['aa', 'bb, cc, dd, ee']