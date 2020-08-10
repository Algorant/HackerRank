# Given an integer, print the first 10 multiples
# each in the form n x i, where each result is
# printed on a new line in form if n x i = result


number = int(input())

def loop(number):
    i = 1
    while i < 11:
        print("{} x {} = {}".format(number,i,(number * i)))
        i += 1

loop(number)
