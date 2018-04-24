# Number
# int、long(廢棄)、float、complex
score = 100
print(type(score))

height = 123.78
print(type(height))

pi = 3.14j
print(type(pi))

# String
name = "我是 Skye，來自新竹，是個前端工程師~"
print(type(name))
print(name)
print(name[0])
print(name[0:2])
print(name * 3)
print(name + " GO")

# List 複數、有順序的集合、長度可變動
list_1 = [1, 2.3, 4j, "String"]
list_2 = ["Skye", "Annie", "Thwu"]
print(type(list_1))
print(len(list_1))
print(list_1 + list_2)
print(list_1 * 2)
for i in list_1:
    print(i)

# Tuple

# Dictionary


# **
print(2 ** 10)

# & 二進制 AND 計算
# | 二進制 OR 計算
# ^ 二進制 XOR 計算
# ~ 二進制 NOT 計算

# for
for i in range(4):
    print(i)

# while
begin = 10
end = 100
step = 10
while (begin < end):
    print(begin)
    begin = begin + step

# if else
score = 60
if score >= 60:
    print("及格")   
else:
    print("不及格")

# if elif lse
score = -1
if score >=0 and score < 60:
    print("不及格")
elif score >= 60 and score <=79:
    print("普通")
elif score >=80 and score <=99:
    print("不錯")
elif score == 100:
    print("滿分")
else:
    print("啥")

