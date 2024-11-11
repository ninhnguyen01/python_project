# Import package
import datetime as dt

today = dt.date.today()
print('Today: ', today)
print()
yesterday = today - dt.timedelta(days=1)
print('Yesterday: ', yesterday)
print()
tomorrow = today + dt.timedelta(days=1)
print('Tomorrow: ', tomorrow)
print()
print('Time between tomorrow and yesterday:', tomorrow - yesterday)
print()