from datetime import datetime


current_date = datetime.now()

print(current_date.year, "- year")
print(current_date.month, "- month")

print(current_date.date(), "- дата в целом")


d1 = datetime(year=1999, month=3, day=14)

print(d1)
