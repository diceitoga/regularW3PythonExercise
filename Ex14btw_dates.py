# Ex 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
#Use code calendar.month(year, month, date)   ->calendar class actually does not work
#import datetime and date funciton as show below; and here-> https://stackoverflow.com/questions/151199/how-to-calculate-number-of-days-between-two-given-dates
from datetime import date

year1 =2014
year2 =2014
month1 =7
month2 =7
date1 = 2
date2 = 11

print(type(year1))
print(type(month1))
print(type(date1))
target_date2 = date(year2,month2,date2)
print(type(target_date2))
target_date1 = date(year1,month1,date1)
print(type(target_date1))
difference = target_date2-target_date1
print(difference)
