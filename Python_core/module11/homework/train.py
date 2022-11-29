
import datetime


birthsday = input('print  a birthsday  [dd.mm.yyyy]  - ')
day, month, year = birthsday.split('.')

# day, month, year = int(day), int(month), int(year)


date = datetime.date(day=int(day), month=int(month), year=int(year))

print(date)
