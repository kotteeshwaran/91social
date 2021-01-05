from  datetime import date
date_1 = date(2020, 7, 2)
date_2 = date(2020, 7, 11)
delta = date_2 - date_1
print("Number of days:{}".format(delta.days))