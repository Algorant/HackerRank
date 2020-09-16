'''
Given a date, use calendar module in python to find what weekday
it is on that date.
'''

import calendar

m, d, y = list(map(int, input().split()))

print((list(calendar.day_name)[calendar.weekday(y, m, d)]).upper())
