# Problem
# The start or end of a string needs to be checked for a specific text pattern, like file extension, URL schemas, etc.

# Solution
# A simple way is to use str.startswith() or str.endswith() methods.
filename = 'spam.txt'
print(filename.endswith('.txt'))  # True
print(filename.startswith('file:'))  # False
url = 'http://www.python.org'
print(url.startswith('http:'))  # True

# If multiple choices need to be checked, provide a tuple of possibilities to the methods.
import os
filenames = os.listdir('.')
print(filenames)
print([name for name in filenames if name.endswith(('.md', '.py'))])
print(any(name.endswith('.py') for name in filenames))  # True

from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

# This is one part of Python where a tuple is required as input.
# If the choices are specified in a list or set, make sure they get
#  converted to tuple() first.

choices = ['http:', 'ftp:']
url = 'http://www.python.org'
try:
    url.startswith(choices)
except Exception as e:
    print(e)
print(url.startswith(tuple(choices)))  # True

# Discussion
# These two methods provide a convenient way to perform basic prefix and suffix checking.
# These operations can also be performed with slices, but are less elegant.
filename = 'spam.txt'
print(filename[-4:] == '.txt')  # True
url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'fps:')  # True

# This can also be done with regex, but is often overkill for simple matching.
import re
url = 'http://www.python.org'
print(re.match('http:|https:|ftp:', url))

# The startswith() and endswith() methods look nice when combined with other operations,
#  like with common data reductions.
if any(name.endswith(('.c', '.h')) for name in listdir(dirname)):
    print('This is a C directory')
