class Person:
    def __init__(self,initialAge):
        # Set initial age equal to zero.
        self.age = initialAge
        if self.age < 0: # make sure age is not negative
            print('Age is not valid, setting age to 0.')
            self.age = 0

    def amIOld(self):
        # Checks for age range and gives various outputs depending
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # adds a year to age as a year passes
        self.age += 1


# This code is for testing purposes according to HackerRank,
# they said don't remove.
t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
