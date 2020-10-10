'''
Given an xml file of length N, find the
score of the file, which is adding up all the tags
and attributes in the file.
'''

import xml.etree.ElementTree as etree

tree = etree.ElementTree(etree.fromstring(xml))

# xml = ''.join(input() for _ in xrange(input()))

def get_attr_number(node):
    return sum(len(child.attrib) for child in node.iter())


# This code is given in problem:

# if __name__ == '__main__':
#     sys.stdin.readline()
#     xml = sys.stdin.read()
#     tree = etree.ElementTree(etree.fromstring(xml))
#     root = tree.getroot()
#     print(get_attr_number(root))
