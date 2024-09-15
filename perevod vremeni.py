import time
import datetime
from datetime import timedelta

dt_now = datetime.datetime.now()  # data today
w_day = dt_now.weekday()  # week day
res_dt = ''  # date from monday

if w_day == 0:
    res_dt = dt_now
elif w_day == 1:
    res_dt = dt_now - timedelta(days=1)
elif w_day == 2:
    res_dt = dt_now - timedelta(days=2)
elif w_day == 3:
    res_dt = dt_now - timedelta(days=3)
elif w_day == 4:
    res_dt = dt_now - timedelta(days=4)
elif w_day == 5:
    res_dt = dt_now - timedelta(days=5)
elif w_day == 6:
    res_dt = dt_now - timedelta(days=6)

date_time = datetime.datetime(int((str((res_dt.date())).split('-'))[0]),
                              int((str((res_dt.date())).split('-'))[1]),
                              int((str((res_dt.date())).split('-'))[2]), 00, 00)

mon_date = str(int((time.mktime(date_time.timetuple())))) + '000'  # id monday !!!!

print('ponedelnik = ' + mon_date)

res_dt = res_dt + timedelta(days=5)
date_time = datetime.datetime(int((str((res_dt.date())).split('-'))[0]),
                              int((str((res_dt.date())).split('-'))[1]),
                              int((str((res_dt.date())).split('-'))[2]), 23, 59, 59)

sun_date = str(int((time.mktime(date_time.timetuple())))) + '999'  # id sunday !!!!
print('voskresenie = ' + sun_date)
