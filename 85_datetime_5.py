#add/subtract days into date
from datetime import datetime as dt
from datetime import timedelta 
now = dt.now()

print(now)

#add 100 days into date object
t1 = timedelta(days=120)

new_date = now.__add__(t1)
print(new_date)

t2 = timedelta(days=-180)

old_date = now.__add__(t2)
print(old_date)
