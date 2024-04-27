import datetime
birth_year = int(input("Enter your birth year: "))
present_year = datetime.date.today().year
age = present_year - birth_year
print("Your age:",age)
