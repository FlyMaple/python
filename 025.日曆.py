import calendar

# props = dir(calendar)
# props.sort()

# for prop in props:
#     print(prop)

"""
Calendar
EPOCH
FRIDAY
February
HTMLCalendar
IllegalMonthError
IllegalWeekdayError
January
LocaleHTMLCalendar
LocaleTextCalendar
MONDAY
SATURDAY
SUNDAY
THURSDAY
TUESDAY
TextCalendar
WEDNESDAY
_EPOCH_ORD
__all__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
_colwidth
_locale
_localized_day
_localized_month
_spacing
c
calendar
datetime
day_abbr
day_name
different_locale
error
firstweekday
format
formatstring
isleap
leapdays
main
mdays
month
month_abbr
month_name
monthcalendar
monthrange
prcal
prmonth
prweek
repeat
setfirstweekday
sys
timegm
week
weekday
weekheader
"""

# 打印日曆
#       May 2018
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31
print(calendar.month(2018, 5, w=0, l=0))
print(calendar.prmonth(2018, 5))

# calendar.(year[, m=3, c=6, l=1, w=2])
# calendar.calendar(year[, m=3, c=6, l=1, w=2])
# m 每橫列有幾個月
# c 每個月間的距離(左右向)
# l 日期間的距離(上下向)
# w 日期間的距離(左右向)
#
#       January               February               March
# Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7            1  2  3  4            1  2  3  4
#  8  9 10 11 12 13 14   5  6  7  8  9 10 11   5  6  7  8  9 10 11
# 15 16 17 18 19 20 21  12 13 14 15 16 17 18  12 13 14 15 16 17 18
# 22 23 24 25 26 27 28  19 20 21 22 23 24 25  19 20 21 22 23 24 25
# 29 30 31              26 27 28              26 27 28 29 30 31

#        April                  May                   June
# Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
#                    1      1  2  3  4  5  6               1  2  3
#  2  3  4  5  6  7  8   7  8  9 10 11 12 13   4  5  6  7  8  9 10
#  9 10 11 12 13 14 15  14 15 16 17 18 19 20  11 12 13 14 15 16 17
# 16 17 18 19 20 21 22  21 22 23 24 25 26 27  18 19 20 21 22 23 24
# 23 24 25 26 27 28 29  28 29 30 31           25 26 27 28 29 30
# 30

#         July                 August              September
# Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
#                    1         1  2  3  4  5                  1  2
#  2  3  4  5  6  7  8   6  7  8  9 10 11 12   3  4  5  6  7  8  9
#  9 10 11 12 13 14 15  13 14 15 16 17 18 19  10 11 12 13 14 15 16
# 16 17 18 19 20 21 22  20 21 22 23 24 25 26  17 18 19 20 21 22 23
# 23 24 25 26 27 28 29  27 28 29 30 31        24 25 26 27 28 29 30
# 30 31

#       October               November              December
# Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7            1  2  3  4                  1  2
#  8  9 10 11 12 13 14   5  6  7  8  9 10 11   3  4  5  6  7  8  9
# 15 16 17 18 19 20 21  12 13 14 15 16 17 18  10 11 12 13 14 15 16
# 22 23 24 25 26 27 28  19 20 21 22 23 24 25  17 18 19 20 21 22 23
# 29 30 31              26 27 28 29 30        24 25 26 27 28 29 30
#                                             31
print(calendar.calendar(2018, c=6, w=2, l=1, m=3))
print(calendar.prcal(2018, c=6, w=2, l=1, m=3))

# 返回 calendar module 一星期的起始日 0 === 星期一
print(calendar.firstweekday())  # 0

# 是否為閏年
print(calendar.isleap(2018))

# 兩個日期間有幾個閏年
print(calendar.leapdays(1970, 2018))

# [[0, 1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27], [28, 29, 30, 31, 0, 0, 0]]
print(calendar.monthcalendar(2018, 5))

# 返回指定月份的 (星期幾開始, 總共有幾日)
#
#    February 2018
# Mo Tu We Th Fr Sa Su
#           1  2  3  4
#  5  6  7  8  9 10 11
# 12 13 14 15 16 17 18
# 19 20 21 22 23 24 25
# 26 27 28
# 返回 (3, 28)
#
#      July 2018
# Mo Tu We Th Fr Sa Su
#                    1
#  2  3  4  5  6  7  8
#  9 10 11 12 13 14 15
# 16 17 18 19 20 21 22
# 23 24 25 26 27 28 29
# 30 31
# 返回 (6, 31)
print(calendar.monthrange(2018, 2))  # (3, 28)
print(calendar.monthrange(2018, 2))  # (6, 31)


# 更改一周起始日
#       May 2018
# Su Mo Tu We Th Fr Sa
#        1  2  3  4  5
#  6  7  8  9 10 11 12
# 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26
# 27 28 29 30 31
calendar.setfirstweekday(6)  # 6 === 星期日
print(calendar.month(2018, 5))
#       May 2018
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31
calendar.setfirstweekday(0)  # 6 === 星期一
print(calendar.month(2018, 5))

# 查看 2018/5/8 是星期幾(代碼)
print(calendar.weekday(2018, 5, 8))