import datetime
import time

# 2021-05-25 11:55:04.196642
# 当前日期
print(datetime.datetime.now())

# 1621914904.1966426
# 当前时间戳
print(time.time())

# Tue May 25 11:55:04 2021
# 当前时间的字符串形式
print(time.ctime())

# time.struct_time(tm_year=2021, tm_mon=5, tm_mday=25, tm_hour=11, tm_min=55, tm_sec=4, tm_wday=1, tm_yday=145, tm_isdst=0)
# 当前时间的sstruct_time形式
print(time.localtime())

# 2021-05-25 11-55-04
# 获取当前时间，可以将时间格式化为字符串
print(time.strftime("%Y-%m-%d %H-%M-%S"))
