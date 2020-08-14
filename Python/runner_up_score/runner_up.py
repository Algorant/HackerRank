# Given integer n and array A of size n,
# find the second highest score


n = int(input())
A = map(int, input().split())

# Basically need to sort, use set to remove duplicates,
# and then select penultimate object [-2]

def runner_up(A):
    # create sorted sorted without dupes
    a_sort = sorted(set(A))
    # return penultimate
    return a_sort[-2]

print(runner_up(A))
