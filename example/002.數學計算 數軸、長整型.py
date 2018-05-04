# 簡述：企業發放的獎金根據利潤提成。利潤(I)低於或等於10萬元時，獎金可提10%；利潤高於10萬元，低於20萬元時，低於10萬元的部分按10%提成，高於10萬元的部分，可提成7.5%；20萬到40萬之間時，高於20萬元的部分，可提成5%；40萬到60萬之間時高於40萬元的部分，可提成3% ；60萬到100萬之間時，高於60萬元的部分，可提成1.5%，高於100萬元時，超過100萬元的部分按1%提成.

# 提問：從鍵盤輸入當月利潤I，求應發放獎金總數？

# 玩蛇網Python解題思路分析：請利用數軸來分界及定位。並要注意定義時需要把獎金定義成長整型的數據類型。
# http://www.iplaypy.com/python-100/7091.html


# raw_input 不再用了
profit = int(input(">>> I: "), 10)

profit_percent_list = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
profit_percent_list_length = len(profit_percent_list)
profit_money_list = [100000, 200000, 400000, 600000, 1000000]
profit_money_list_length = len(profit_money_list)

for i, p in enumerate(profit_money_list):
    a, b = 0, 0

    if profit <= profit_money_list[0]:
        a = profit * profit_percent_list[0]
    else:
        if i+1 < profit_money_list_length:
            if profit > p and profit <= profit_money_list[i+1]:
                a = profit_money_list[i] * profit_percent_list[i]
                b = (profit - p) * profit_percent_list[i+1]
        else:
            a = profit_money_list[profit_money_list_length-1] * profit_percent_list[i]
            b = (profit - profit_money_list[profit_money_list_length-1]) * profit_percent_list[profit_percent_list_length-1]

    if a != 0 or b != 0:
        print('A: {}'.format(a))
        print('B: {}'.format(b))
        break