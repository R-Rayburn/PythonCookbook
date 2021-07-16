# Problem
# You want to match text with wildcard patters that are commonly used in Unix shells.
# (e.g., *.py,Dat[0-9]*.csv, etc.)

# Solution
# fnmatch module provides tow functions that can perform this matching: fnmatch() and fnmatchcase()
from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))  # True
print(fnmatch('foo.txt', '?oo.txt'))  # True
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))  # True
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])

# Normally, fnmatch() will match patterns using the case-sensitive rules as the system's underlying filesystem.

# On OS X (Mac)
print(fnmatch('foo.txt', '*.TXT'))  # False
# On Windows
print(fnmatch('foo.txt', '*.TXT'))  # True

# If distinction matters, use fnmatchcase() to match exactly based on the lower and uppercase
#  conventions supplied.
print(fnmatchcase('foo.txt', '*.TXT'))  # False

# An overlooked feature of these functions is their use with data processing of nonfilename strings.
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])

# Discussion
# Matching performed by fnmatch is between the functionality of simple string methods and
#  regexes. If trying to provide a simple mechanism for allowing wildcards in data processing, it
#  is a resonable solution.
# If you need code that matches filenames, use the glob module instead (Recipe 05.13)
