'''
Given the sequence of up and down steps during a hike, find and print the
number of valleys walked through.
'''

# This code goes under the given function countingValleys on HackerRank.

sea_level = 0
valley = 0

for i in s:
    if sea_level == 0 and i == 'D':
        valley += 1
    if i == 'U':
        sea_level += 1
    if i == 'D':
        sea_level -= 1

return valley
