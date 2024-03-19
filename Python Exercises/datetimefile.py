# date time 1

import time
seconds = time.time()
print("Time inUTC ",seconds)


# date time 2

import time
current = time.localtime(time.time())
print("Time in current ", current)

# date time 3

import time
current= time.localtime(time.time())
print("Year = ",current.tm_year)
print("Month = ",current.tm_mon)
print("Date = ",current.tm_date)
print("day = ",current.tm_mday)
print("Weekday = ",current.tm_wday)
print("Year day = ",current.tm_yday)
print("Hour = ",current.tm_hour)
print("minutes = ",current.tm_min)
print("Seconds = ",current.tm_sec)


#date time 4
import time
now = time.time()
a=input("Enter a name = ")
later = time.time()
diff=int(later-now)
print(now)
print(later)
print(diff)


#date time 5
import time
print("this is printed immediately")
time.sleep(3)
print("this is printed 3 seconds  later ")


#date time 6
import calendar
cal= calendar.month(2020,1)
print(cal)


#date time 7
import datetime
current = datetime.datetime.now()
print(current)

#date time 8
import datetime
current= datetime.datetime.today()
print(current)

#date time 9
from datetime import date
today= date.today()

print("Current year = ",today.year)
print("Current Month = ",today.month)
print("Current day = ",today.day)
print(today.year,"/",today.month,"/",today.day)

#date time 10
import datetime
date = datetime.datetime(2021,1,17)
print(date)

#datetime 11
import  datetime
today=datetime.date.today()
bday=datetime.date(2000,3,14)
age = today-bday
print(age)
print("in years ",age/365)


#datetime 12
import datetime
d= datetime.datetime(2020,6,26,00,57,47)
print(d)

#datetime 13
import datetime
starttime=datetime.datetime(2020,6,26,00,57,47)
currttime=datetime.datetime.now()
print(starttime,currttime)
while currttime<starttime:
    print("Hello, ", datetime.datetime.now())
    currttime=datetime.datetime.now()
    
    
