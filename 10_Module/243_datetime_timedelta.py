import datetime

now = datetime.datetime.now()

for day in range(5, -1, -1):
    delta = datetime.timedelta(days=day)
    print(now-delta)
