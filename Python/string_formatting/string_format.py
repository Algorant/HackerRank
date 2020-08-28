# Padding
# '{:10}'.format('n') where 10 is the amount to pad by.

# Conversion for padding width:
# {:d} is integer, {:o} is octal, {:X} is hexadecimal, {:b} is binary


def print_formatted(number):
    width = len("{0:b}".format(number))
    for i in range(1, number+1):
        print("{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}".format(i=i,
                width=width))
