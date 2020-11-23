'''
Print the HTML tags and attribute values in order of their
occurrence from top to bottom in the given snippet
'''

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

parser = MyHTMLParser()

for i in range(int(input())):
    parser.feed(input())
