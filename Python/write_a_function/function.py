# Write a function that takes a calendar year as input
# and returns whether it is a leap year or not



# if __name__ == __main__:
# year = int(input())


def is_leap(year):
    """ Function that determines if year is leap or not."""
    if year % 4 == 0 and year % 400 == 0:
        return True
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# Take input of calendar year
year = int(input())

# Show result
print(is_leap(year))
