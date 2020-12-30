import calendar
print(dir(calender))
days = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}
day_in_week = calendar.weekday(2020,12,30)
print(days[day_in_week]) # Wednesday