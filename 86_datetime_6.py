#add/subtract minutes/hours into datetime
from datetime import datetime as dt
from datetime import timedelta 
now = dt.now()

print(now)

#add 100 days into date object
t1 = timedelta(hours=3,minutes=15)

new_date = now.__add__(t1)
print(new_date)

t2 = timedelta(seconds=300)

new_date_2 = now.__add__(t2)
print(new_date_2)
