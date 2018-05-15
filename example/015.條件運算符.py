# 要求：獲取輸入的內容，並利用條件運算符的嵌套方式來完成這道題。
# 學習成績>=90分的同學用A表示，60-89分之間的用B表示，60分以下的用C表示。

score = int(input("Input score: "), 10)

if score >= 90:
    print("A")
elif score > 60 and score <=89:
    print("B")
else:
    print("C")
