# timestamp time between 01-jan-1970 12:00 midnight to current date time 
# epoch time @ 01-jan-1970 12:00

from datetime import datetime as dt 

timestamp = dt.now().timestamp()
timestamp = int(timestamp)

#add 1 day 
timestamp = timestamp + (3600 * 24 * 365)
print(dt.fromtimestamp(timestamp))

