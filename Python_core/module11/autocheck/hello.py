from datetime import datetime, date


class Birthday:
    def __init__(self, name, brth):
        self.cur_date = date.today()
        self.name = name
        d, m, y = brth.split('.')
        self.brth = date(day=int(d), month=int(m), year=int(y))
        # self.near_dr = date(day=int(d), month=int(m), year=self.cur_year)

    # for using this method without  parentheses (скобок)
    # use @property

    def days_to_birthday(self):
        if self.cur_date.month < self.brth.month:
            self.delta_days = date(
                day=int(self.brth.day), month=int(self.brth.month), year=int(self.cur_date.year))
            return self.delta_days - self.cur_date
        else:
            self.delta_days = date(
                day=int(self.brth.day), month=int(self.brth.month), year=int(self.cur_date.year)+1)
            return self.delta_days - self.cur_date


per_1 = Birthday('bogdan', '03.12.2002')
per_2 = Birthday('sasha', '14.08.2003')

cur_date = date.today()


print(per_1.days_to_birthday())
