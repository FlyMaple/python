import datetime

# ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']
print(dir(datetime))

# ['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']
print(dir(datetime.datetime))

# datetime.datetime(2018, 5, 9, 17, 40, 43, 565879)
print(datetime.datetime.now())
print(type(datetime.datetime.now()))  # <class 'datetime.datetime'>

# ['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']
print(dir(datetime.datetime.now()))

# '2018-05-09 17:48:04'
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# datetime.date(2018, 5, 9)
print(datetime.datetime.now().date())
print(datetime.date.today())

# datetime.date(2018, 5, 10)
print(datetime.date.today() + datetime.timedelta(days=1))
# datetime.datetime(2018, 5, 6, 18, 16, 54, 992631)
print(datetime.datetime.now() - datetime.timedelta(days=3))

# ['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'ctime', 'day', 'fromordinal', 'fromtimestamp', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'min', 'month', 'replace', 'resolution', 'strftime', 'timetuple', 'today', 'toordinal', 'weekday', 'year']
print(dir(datetime.date))

# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'dst', 'fold', 'hour', 'isoformat', 'max', 'microsecond', 'min', 'minute', 'replace', 'resolution', 'second', 'strftime', 'tzinfo', 'tzname', 'utcoffset']
print(dir(datetime.time))

# ['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 'days', 'max', 'microseconds', 'min', 'resolution', 'seconds', 'total_seconds']
print(dir(datetime.timedelta))

# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getinitargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'dst', 'fromutc', 'max', 'min', 'tzname', 'utc', 'utcoffset']
print(dir(datetime.timezone))

# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'dst', 'fromutc', 'tzname', 'utcoffset']
print(dir(datetime.tzinfo))


# datetime.datetime.combine
# <built-in method combine of type object at 0x000000006F411D40>
# datetime.datetime(2018, 5, 11, 0, 0)
print(datetime.datetime.combine(datetime.date.today(), datetime.time.min))
# datetime.datetime(2018, 5, 11, 23, 59, 59, 999999)
print(datetime.datetime.combine(datetime.date.today(), datetime.time.max))


# datetime.timedelta(0, 14400)
print(datetime.datetime(2018, 5, 11, 12) - datetime.datetime(2018, 5, 11, 8))
print((datetime.datetime(2018, 5, 11, 12) -
       datetime.datetime(2018, 5, 11, 8)).total_seconds())

# 本周最後一天
today = datetime.date.today()
last_day = today + datetime.timedelta(6 - today.weekday())

# 本月最後一天
import calendar
today = datetime.date.today()
month_days = calendar.monthrange(today.year, today.month)[1]
last_day = datetime.date(today.year, today.month, month_days)

# 上個月最後一天
import calendar
today = datetime.date.today()
last_day = today - datetime.timedelta(today.day)


# 時間轉換
# datetime object / string / timestamp / time tuple
now = datetime.datetime.now()  # datetime object
_str_time = now.strftime('%Y-%m-%d %H:%M:%S')  # string
_timestamp_time = now.timestamp() # timestamp
_tuple_time = now.timetuple() # time tuple
