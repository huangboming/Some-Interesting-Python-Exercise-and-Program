## 判断今天的日期和当前的时间--只用time.time()函数

在《Think Python》第五章中有一个练习：
> The time module provides a function, also named time, that returns the current Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970.
>```python
>>> import time
>>> time.time()
>output: 1437746094.5735958
>```
> Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, plus the number of days since the epoch.

```time.time()```的返回值是从1970年1月1日0:00:00到现在的总秒数（时区为格林威治标准时间（GMT/UTC），中国所在时区为UTC+8）。 题目要求用它的返回值求从1970年1月1日0:00:00到现在的总小时数，总分钟数，总秒数，总天数。

我自己将这个题目拓展为根据```time.time()```求现在的日期和时间。实现起来也不算很难，但还是挺有挑战性的，过程也很有意思。

PS: 如果不要求一定用```time.time()```，可以偷懒一点，用datetime模块五行结束：
```python
from datetime import datetime
import re

pttn = '\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d'
current_time = ''.join(re.findall(datetime.now()))
print(current_time)
```