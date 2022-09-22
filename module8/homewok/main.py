from datetime import datetime, date
import calendar

for _ in range(20):
    print()


users = [
    {"name": "Oksana", "birthday": datetime(year=1999, month=3, day=20)},
    {"name": "Denis", "birthday": datetime(year=1989, month=9, day=22)},
    {"name": "Bogdan", "birthday": datetime(year=2002, month=9, day=17)},
    {"name": "Oleg", "birthday": datetime(year=2006, month=9, day=21)},
    {"name": "Kush", "birthday": datetime(year=1996, month=9, day=22)},
    {"name": "Remi", "birthday": datetime(year=1996, month=9, day=20)},
    {"name": "Lapik", "birthday": datetime(year=1996, month=9, day=22)},
    {"name": "Uraboros", "birthday": datetime(year=1996, month=9, day=23)}
]

#    ------------------------------


print("\n{:=^50}\n".format("-Birthday-"))


# На случай дня предыдущего месяца


# current_month -= 1
# weeks_list = calendar.monthcalendar(current_year, current_month)
# print(weeks_list)


def get_birthday_per_week(users_list):
    current_month = date.today().month

    result = {}

    for person in users_list:

        Month, Day = person['birthday'].month, person['birthday'].day
        cur_year = date.today().year
        cur_day = date.today().day
        birthday = date(cur_year, Month, Day)
        if Month != current_month:
            print("***")
            continue

        print(f'My name is {person["name"]} and my birthday {Month}-{Day}')

        print(f"Date of celebration - {birthday}")
        print(f"{birthday.strftime('%A %d-%m-%y')}")
        week_day = birthday.strftime('%A')
        weeks_list = calendar.monthcalendar(cur_year, Month)

        print()
        for week in weeks_list:
            if cur_day in week:
                cur_week = week
                ind = weeks_list.index(week)
                pre_week = weeks_list[ind-1]
                working_week = pre_week[-2:]+cur_week[0:-2]

                if Day not in working_week:
                    print("Not this time")
                    continue

                print(f"Сurrent week - {cur_week}")
                print(f"Previos week - {pre_week}")
                print(f"Working week - {working_week}")

                if Day in working_week[0:2]:
                    if 'Monday' in result:
                        result['Monday'].append(person['name'])
                    else:
                        result['Monday'] = []
                        result['Monday'].append(person['name'])
                else:
                    if birthday.strftime('%A') in result:
                        result[week_day].append(person['name'])
                    else:
                        result[week_day] = []
                        result[week_day].append(person['name'])

                print(f"result is - {result}")
                break
            else:
                continue
        print("*"*10)
        for day in result:
            print(f"{day}: {', '.join(result[day])}")

        return "DONE!"


print(get_birthday_per_week(users))


#    for person in users_list:
#         for week in weeks_list:
#             if person['birthday'].day in week:
#                 print('here')
#                 count_week = weeks_list.index(person['birthday'].day)
#                 break
#             else:
#                 continue

#         print(weeks_list[count_week])
#         print(person['birthday'].day)
