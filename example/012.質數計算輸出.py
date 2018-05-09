# 簡述：區間範圍101-200

# 要求：判斷這個區間內有多少個素數，並逐一輸出。

count = 0

for i in range(101, 201):
    match = False

    for j in range(2, i):
        if i % j == 0:
            match = True
            break
            
    if match == False:
        print(i)
        count += 1

print("101 ~ 200 有 {}個質數.".format(count))