'''
Given list of integers of length T, separated by /n,
check if that number is prime and return "Prime" or "Not Prime" for
that integer.
'''


# This was first attempt. Naive approach that works but fails 2 test cases
# due to timeout! (Too slow)
# def ptest(T):
#     # Make sure greater than 1
#     if T > 1:
#         # Check if its even or has any other factors
#         for i in range(2, T):
#             if (T % i) == 0:
#                 print("Not Prime")
#                 break # can end if it finds any
#         else:
#             print("Prime") # no factors other than 1 and self
#
#     else:
#         print("Not Prime") # any other case not prime
#
#
# ptest(31)
# ptest(12)
# ptest(33)

# Attempt 2

def prime(num):
    if num == 1:
        return False
    else:
        return all((num % r) for r in range(2, round(num ** 0.5) + 1))
        
T = int(input())
for i in range(1, T+1):
    num = int(input())
    if prime(num)==True:
            print("Not prime")
    else:
        print("Prime")
