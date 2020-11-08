'''
You are given an HTML code snippet of N lines.
Your task is to print start tags, end tags and empty tags
separately.
'''

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Start : {0}".format(tag))
        for attribute in attrs:
            print('->', attribute[0], '>', attribute[1])

    def handle_endtag(self, tag):
        print("End   : {0}".format(tag))

    def handle_startendtag(self, tag, attrs):
        print("Empty : {0}".format(tag))
        for attribute in attrs:
            print('->', attribute[0], '>', attribute[1])

parser = MyHTMLParser()
n = int(input())

for i in range(n):
    parser.feed(input())
