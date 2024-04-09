import calendar
y=int(input("Enter Year:"))
if calendar.isleap(y):
    print(y,'is leap year')
else:
    print(y,'is not leap year')
