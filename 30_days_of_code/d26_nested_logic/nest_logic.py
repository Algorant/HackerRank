'''
Take inputs of grigorian dates that:
-a book was rented
-a book was returned
and return the fee due depending on how late the book
was in being returned.
'''


'''
This was my initial approach, using datetime
and trying to just do it as functional and human-readable
as possible just to get something going.
'''

# import datetime
#
# day_rented = input()
# day_return_expected = input()
#
# days_late = day_rented.date() - day_return_expected.date()
#
# def fine(days_late):
#     if days_late > 15:
#         return 15 * days_late
#
#     elif days_late > 30:
#         return (days_late / 30) * 500
#
#     else:
#         return 10000

'''
It's actually way easier to do this using python tuple comparison.
I learned a new skill today!
'''

# Take the input for date day_rented as a day, month, year tuple
rd, rm, ry = [int(x) for x in input().split(' ')]

# Take the input for date expected_return as a day, month, year tuple
ed, em, ey = [int(x) for x in input().split(' ')]

# No fee condition, the day returned is less or equal to day rented
if (ry, rm, rd) <= (ey, em, ed):
    print(0)

# Daily fee condition, charged 15 hackos per day up to 30 days_late
elif (ry, rm) == (ey, em): # make sure year and month are same
    print(15 * (rd - ed))

# Monthly fee condition, charged 500 hackos per month up to 1 year late
elif ry == ey:
    print(500 * (rm - em))

# Yearly fee condition, if years are different its 10,000 hackos!

else:
    print(10000)
