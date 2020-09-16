'''
Given two timestamps as input, find the time delta between them
'''



# Datetime module has useful strptime function for this purpose
from datetime import datetime as dt


def time_delta(t1, t2):
    # take the times as inputs
    date1 = dt.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    date2 = dt.strptime(t2, "%a %d %b %Y %H:%M:%S %z")

    # return the delta
    a = abs(int((date1 - date2).total_seconds()))
    return str(a)
