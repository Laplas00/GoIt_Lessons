from datetime import date, datetime
import calendar


from datetime import date


def get_days_in_month(month, year):
    if month == 12:
        new_month = 1
        new_year = year+1
    else:
        new_month = month+1
        new_year = year

    first_date = date(new_year, new_month, 1)
    sec_date = date(year, month, 1)
    print("FIRST_DATE", first_date)
    print("SEC_DATE", sec_date)
    res = first_date - sec_date
    print(res)
    return res.days


get_days_in_month(12, 2022)
