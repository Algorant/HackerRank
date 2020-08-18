# In this challenge create class Mybook which inherits from Book,
# and given input of title, author, price, print each using a @method
# called display.


from abc import ABCMeta, abstractmethod
class Book(self, object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author

class MyBook(Book):
    # initialize mybook class
    def __init__(self, title, author, price):
        # inherit from book
        Book.__init__(self, title, author)
        self.price = price
    # create display method to print output
    def display(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Price: {}".format(self.price))
