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
            days_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            
        i = 0
        while days >= 0 and 0 <= i < 12:
            days -= days_list[i]
            total_month += 1
            i += 1
        start_year += 1
        
    todays_month = int(total_month - (todays_year(start_year, total_days) - start_year) * 12) # 现在的月份 = 总月数 - 年数差 x 12
    todays_day = int(days + days_list[todays_month]) # 现在的日期 = 剩下几天到下一个月1号（负数） + 这个月的天数
    
    
    return [todays_month, todays_day] ## 返回今天的月份和日期



def main():
    total_seconds = time.time() ## time.time()返回从1970年1月到现在总共过了多少秒
    total_minutes = time.time() // 60 ## 分 = 秒 / 60（向下取整，下同）
    total_hours = total_minutes // 60 ## 小时 = 分 / 60
    total_days = total_hours // 24 ##  天 = 小时 / 24
    start_year = 1970 ## time.time()从1970年1月开始计算

    todaysYear = todays_year(start_year, total_days) # 当前的年份
    todaysMonth, todaysDay = todays_month(start_year, total_days) # 当前的月份和日期

    nowsHour = int(total_hours - total_days * 24) # 现在的小时数 = 总小时数 - 总天数 * 24
    nowsMinute = int(total_minutes - total_hours * 60) # 现在的分钟数 = 总分钟数 - 总小时数 * 60
    nowsSecond = int(total_seconds - total_minutes * 60) # 现在的秒数 = 总秒数 - 总分钟数 * 60
    
    print(f"Now is {todaysYear}-{todaysMonth}-{todaysDay}  {nowsHour}:{nowsMinute}:{nowsSecond} GMT")
    print(f"Now is {todaysYear}-{todaysMonth}-{todaysDay}  {nowsHour + 8}:{nowsMinute}:{nowsSecond} UTC +8")
    
if __name__ == "__main__":
    main()