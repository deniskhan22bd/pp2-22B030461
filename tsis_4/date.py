import datetime

#1
"""
date = datetime.datetime.today()
print(date)
print(date - datetime.timedelta(days= 5))
"""

#2
"""
date = datetime.datetime.today()
print("Yesterday", date - datetime.timedelta(days= 1))
print("Today", date)
print("Tomorrow", date + datetime.timedelta(days= 1))
"""

#3
"""
date = datetime.datetime.today().replace(microsecond= 0)
print(date)
"""

#4
"""
date1 = datetime.datetime(year= 2023, month= 1, day= 13)
date2 = datetime.datetime.now()

print((date2 - date1).days * 60 * 3600 + (date2 - date1).seconds)
"""