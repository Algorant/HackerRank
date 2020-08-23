# Write a funciton that takes in input s, and returns
# whether or not s is a palindrome.



# This is a very simple way to write the function, but
# the exercize asks for it in a different format:

# def isPalindrome(s):
#     s == s[::-1]


class Solution:
    def __init__(self):
        self.mystack = list()
        self.myqueue = list()
        return(None)

    # Pushes character onto stack
    def pushCharacter(self, char):
        self.mystack.append(char)

    # Returns character to top of stack
    def popCharacter(self):
        return(self.mystack.pop(-1))

    # Puts character into enqueue variable
    def enqueueCharacter(self, char):
        self.myqueue.append(char)

    # Dequeues and returns first character
    def dequeueCharacter(self):
        return(self.myqueue.pop(0))
