# This challenge asks you to take n inputs and then performs n commands
# on a given list. They can be print, insert, append, reverse, etc. If the
# command is print, print the line.

# Begin with empty list

list = []

# iterate through commands, and expand what is after command
for _ in range(int(input())):
    command, *value = input().split()
    # if command is print, print
    if command == 'print':
        print(list)
    else: # otherwise, get attribute and iterate again
        getattr(list, command)(*(map(int, value)))
