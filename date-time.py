from datetime import datetime
from datetime import date
from datetime import time

now = datetime.now()
print(now)
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
print(f"Today: {day}/{month}/{year}  time: {hour}H {minute}M")

date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

d = date.today()
print("Current year:", d.year)
print("Current month:", d.month)
print("Current day:", d.day)

a = time()
print(a)
b = time(10, 30, 20)
print(b)

today = date(2022, 12, 29)
new_year = date(2023, 1, 1)
time_left = new_year - today
print(time_left)
