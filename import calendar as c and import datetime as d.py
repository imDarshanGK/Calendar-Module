import calendar as c
import datetime as d
print(c.calendar(2024))
print(c.month(2024,4))
print(c.isleap(2024))
print(c.weekday(2024,4,8))
print(d.date.today().weekday())
print(d.date.today().month)
print(c.day_name[d.date.today().weekday()])
print(c.month_name[d.date.today().month])
