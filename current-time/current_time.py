# Think Python -- Chapter 5 Exercise 1

# The time module provides a function, also named time, that returns the current Greenwich Mean Time in “the epoch”, 
# which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970.
# >>> import time
# >>> time.time()
#   1437746094.5735958
# Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, 
# plus the number of days since the epoch.

"""判断今天的日期和当前的时间（GMT & UTC+8）--只用time.time()函数"""

import time

def is_leap(year): #判断year是否是闰年
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def todays_year(start_year, total_days): #计算今年年份
    while total_days >= 366:
        start_year += 1
        if not is_leap(start_year):
            total_days -= 365
        else:
            total_days -= 366
            
    return start_year

def todays_month(start_year, total_days): #计算今天的月份和日期
    total_month = 0
    days = total_days
    
    while days >= 0:  # 计算从1970年1月到今天的总月份
        if is_leap(start_year):
            days_list = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            days_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            
        month = 1
        while days >= 0 and 1 <= month <= 12:
            days -= days_list[month]
            total_month += 1
            month += 1
        start_year += 1
        
    todays_month = int(total_month - (todays_year(start_year, total_days) - start_year) * 12) # 现在的月份 = 总月数 - 年数差 x 12
    todays_day = int(days + days_list[todays_month]) # 现在的日期 = 剩下几天到下一个月1号（负数） + 这个月的天数
    
    
    return [todays_month, todays_day] ## 返回今天的月份和日期



def main():
    total_seconds = time.time() 
    total_minutes, nowsSecond = divmod(time.time(), 60)
    total_hours, nowsMinute = divmod(total_minutes, 60) 
    total_days, nowsHour = divmod(total_hours, 24)
    start_year = 1970 

    todaysYear = todays_year(start_year, total_days) # 当前的年份
    todaysMonth, todaysDay = todays_month(start_year, total_days) # 当前的月份和日期

    gmt_time_tuple = (todaysYear, todaysMonth, todaysDay, nowsHour, nowsMinute, nowsSecond)
    utc_8_time_tuple = (todaysYear, todaysMonth, todaysDay, nowsHour+8, nowsMinute, nowsSecond)
    
    print("Now is %d-%.2d-%.2d  %.2d:%.2d:%.2d GMT" % gmt_time_tuple) 
    print("Now is %d-%.2d-%.2d  %.2d:%.2d:%.2d UTC +8" % utc_8_time_tuple)
    
if __name__ == "__main__":
    main()