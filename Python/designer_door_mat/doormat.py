'''
Takes in integer inputs n and m and returns a doormat style design
that has dimensions n x m
'''

n = int(input())
m = int(input())

def doormat(n,m):
    # Print the top part
    for i in range(1,n,2):
        print((i *".|.").center(m, "-"))
    # Print the center
    print("WELCOME".center(m,"-"))
    # Print the bottom
    for i in range(n-2, -1, -2):
        print((i * ".|.").center(m, "-"))


print(doormat(n,m))
