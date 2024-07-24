import calendar
import locale
from datetime import date
import time


hallower = date(2023,7,24)
countri = ['en-us']
locale.setlocale(locale.LC_TIME, countri)
print(hallower.strftime('%A,%B %d'))

now = date.today()
delt = now - hallower
print(hallower)
print(delt)

print(time.ctime(time.time()))