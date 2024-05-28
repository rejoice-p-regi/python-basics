year = int(input("enter a year : "))
import calendar
if calendar.isleap(year):
    print("it is a leap year")
else:
    print("it is not a leap year")