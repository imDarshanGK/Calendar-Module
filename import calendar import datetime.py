import calendar
import datetime
print(calendar.calendar(2024))
print(calendar.month(2024,5))
print(calendar.isleap(2024))
print(calendar.weekday(2024,5,8))
print(datetime.date.today().weekday())
print(datetime.date.today().month)
print(calendar.day_name[datetime.date.today().weekday()])
print(calendar.month_name[datetime.date.today().month])
