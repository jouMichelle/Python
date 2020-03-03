# Python关于时间的标准库

#  time标准库一般会用于时间的查看
import time

# 打印出1971年1月1日至今所经历的秒数
print(time.time())
# 打印当前时间
print(time.localtime())
# 打印格式化的当前时间
print(time.strftime('%Y-%m-%d %H:%M:%S'))

#  datetime 标准库一般用于时间的修改或偏移
import datetime

# 打印当前时间
print(datetime.datetime.now())
# 打印当前时间十分钟之后的时间
newtime = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + newtime)
# 查看指定时间之后的十天的日期
one_day = datetime.datetime(2008, 5, 27)
new_date = datetime.timedelta(days=10)
print(one_day + new_date)
