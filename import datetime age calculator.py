import datetime
by=int(input("Enter your birth year:"))
py=datetime.date.today().year
age=py-by
print("Your age=",age)
