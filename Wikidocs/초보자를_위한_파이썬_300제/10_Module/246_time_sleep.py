import datetime
import time

while True:
    now = datetime.datetime.now()
    print(now.strftime("%H:%M:%S"))
    time.sleep(1)
