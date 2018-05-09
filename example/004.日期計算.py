# 簡述：要求輸入某年某月某日
# 提問：求判斷輸入日期是當年中的第幾天？
import time
import calendar

input_year, input_month, input_day, total_day = 0, 0, 0, 0
month_day_list = []

def get_input():
    global input_year, input_month, input_day

    input_year = int(input('Year: '), 10)
    input_month = int(input('Month: '), 10)
    input_day = int(input('Day: '), 10)


def set_month_day_list(year):
    for m in range(12):
        month = m + 1

        if month == 2:
            if calendar.isleap(year):
                month_day_list.append(29)
            else:
                month_day_list.append(28)
        else:
            m_range = calendar.monthrange(input_year, month)
            month_day_list.append(m_range[1])


def calc():
    global total_day

    for m_day in month_day_list[0:input_month - 1]:
        total_day = total_day + m_day

    total_day = total_day + input_day


get_input()
set_month_day_list(input_year)
calc()

print("{}/{}/{} 為當年中第: {}天".format(str(input_year), str(input_month), str(input_day), str(total_day)))
