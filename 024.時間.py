import time

# props_list = dir(time)
# props_list.sort()
# for prop in props_list:
#     print(prop)

"""
_STRUCT_TM_ITEMS
__doc__
__loader__
__name__
__package__
__spec__
altzone
asctime
clock
ctime
daylight
get_clock_info
gmtime
localtime
mktime
monotonic
perf_counter
process_time
sleep
strftime
strptime
struct_time
time
timezone
tzname
"""

# -32400
print(time.altzone)

# 取得格式化時間
# Fri May  4 16:01:00 2018
print(time.asctime())
# <class 'str'>
print(type(time.asctime()))

# 61.40763370423106
print(time.clock())

# 'Fri May  4 16:48:46 2018'
print(time.ctime())

# 0
print(time.daylight)

#
time.get_clock_info

# time.struct_time(tm_year=2018, tm_mon=5, tm_mday=4, tm_hour=8, tm_min=51, tm_sec=55, tm_wday=4, tm_yday=124, tm_isdst=0)
print(time.gmtime())
# <class 'time.struct_time'>
print(type(time.gmtime()))

"""
tm_year	2008
tm_mon	1 到12
tm_mday	1 到31
tm_hour	0 到23
tm_min	0 到59
tm_sec	0 到61 (60或61 是閏秒)
tm_wday	0到6 (0是周一)
tm_yday	1 到366(儒略歷)
tm_isdst	-1, 0, 1, -1是決定是否為夏令時的旗幟
"""
# time.struct_time(tm_year=2018, tm_mon=5, tm_mday=4, tm_hour=16, tm_min=54, tm_sec=33, tm_wday=4, tm_yday=124, tm_isdst=0)
print(time.localtime())
#time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
print(time.localtime(0))

# 元組時間 轉 時間戳
# 1525428337.0
print(time.mktime(time.localtime()))

# 101442.843
print(time.monotonic())

# 774.5671204811589
print(time.perf_counter())

# 0.140625
print(time.process_time())

# 類似 delay 效果
time.sleep(5)

# 格式化時間
# 元組時間 轉 格式化字串
# strftime(format[, t])
# '2018-05-04 17:52:57'
print(time.strftime("%Y-%m-%d %H:%M:%S"))
# Fri May 04 18:02:24 2018
print(time.strftime("%a %b %d %H:%M:%S %Y"))
# 2018-05-04 17:53:55
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 格式化字串 轉 元組時間
# strptime(str_time[, format])
str_time = "Sat Mar 28 22:24:24 2016"
# time.struct_time(tm_year=2016, tm_mon=3, tm_mday=28, tm_hour=22, tm_min=24, tm_sec=24, tm_wday=5, tm_yday=88, tm_isdst=-1)
print(time.strptime(str_time))
# time.struct_time(tm_year=2016, tm_mon=3, tm_mday=28, tm_hour=22, tm_min=24, tm_sec=24, tm_wday=5, tm_yday=88, tm_isdst=-1)
print(time.strptime(str_time, "%a %b %d %H:%M:%S %Y"))

#
time.struct_time

# 當前的時間戳
# 1525424600.1841576
print(time.time())

# -28800
print(time.timezone)

#
print(time.tzname)
