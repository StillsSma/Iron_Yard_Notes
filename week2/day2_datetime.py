import datetime

# 3-1-2015

day = datetime.datetime(year=2004, month=3, day=1)
#print (day - datetime.timedelta(hours=12)

now = datetime.datetime.now()

print(now.strftime("%A, %B, %Y "))
