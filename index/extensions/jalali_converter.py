'''
Jalali calender Converter V 0.0.1
Dev : #ABS
'''

from django.utils import timezone
from jalali_date import datetime2jalali

def jalali_converter(time):
    # This function returns jalali calendar output
    jmonths = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    time = datetime2jalali(time)
    time_str = time.strftime("%Y, %m, %d, %H,%M,%S")
    time_list = time_str.split(",")

    for index, month in enumerate(jmonths):
        if int(time_list[1]) == index + 1:
            time_list[1] = month
            break

    output = "{} / {} / {}, ساعت {} : {} : {}".format(
        time_list[2],
        time_list[1],
        time_list[0],
        time_list[3],
        time_list[4],
        time_list[5],
    )

    return output