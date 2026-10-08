from datetime import datetime as dt 

date = dt.now()
print(date)
week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
today = week[date.weekday()] + " " + str(date.day) + "/" + str(date.month) + "/" + str(date.year)
print("today is ",today)
time =str(date.hour) + ":" + str(date.minute)
print(time)