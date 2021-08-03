# Problem
# There is text that you want to match or search with a specific pattern.

# Solution
# If you are trying to match a simple literal, you can often just use the basic
#  string methods.
text = 'yeah, but no, but yeah, but no, but yeah'

# Exact match
print(text == 'yeah')  # False
# Match at start or end
print(text.startswith('yeah'))  # True
print(text.endswith('no'))  # False
# Search for the location of the first occurrence
print(text.find('no'))  # 10

# For more complicated matching, prefer regexes with the re module.
# An example is that you want to match dates specified as digits, such as
#  "11/27/2021"
text1 = '11/27/2021'
text2 = 'Nov 27, 2021'

import re
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

# If you are going ot perform a lot of matches using the same pattern, it is a good idea
#  to precompile the regex into a pattern obj.
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')
if datepat.match(text2):
    print('yes')
else:
    print('no')

# match() tries to find the match at teh start of a string. To search for all occurrences in a text, use
#  findall()
text = 'Today is 11/27/2021. PyCon starts 3/13/2022.'
print(datepat.findall(text))

# When defining regex patterns, it is common to introduce capture
#  groups by enclosing parts of the pattern in paenthesis.
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

# Capture groups can simplify subsequent processing of matched text
#  because the contents of each group cna be extracted individaully.
m = datepat.match('11/27/2021')
print(m)
# Extract contents of each group
print(m.group(0))  # '11/27/2021'
print(m.group(1))  # '11'
print(m.group(2))  # '27'
print(m.group(3))  # '2021'
print(m.groups())  # ('11', '27', '2021')
month, day, year = m.groups()
# Find all matches
print(text)
print(datepat.findall(text))
for m, d, y in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# findall() searches the text and finds all matches, returning a list.
# If you want matches iteratively, use finditer() instead.
for m in datepat.finditer(text):
    print(m.groups())

# Discussion
# This recipe discusses teh basics of using the re module to match and search for text.
# The essential functionality is compiling a pattern using re.compile() then use methods
#  like match(), findall(), or finditer()
# When specifying patterns, it is common to use raw strings such as r'(\d+)/(\d+)/(\d+)'.
# These strings leave the backslash character uninterpreted, otherwise, you need to use
#  double backslashes '(\\d+)/(\\d+)/(\\d+)'.

# Note match() only checks the beginning of a string. It could match things you don't expect
m = datepat.match('11/27/2021abcdef')
print(m)
print(m.group())

# Use the end-marker ($) if you want an exact match.
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(datepat.match('11/27/2021abcdef'))
print(datepat.match('11/27/2021'))

# If you're just doing simple matching/searching in text, you can
#  often skip compilation and use module-level functions in the re module.
print(re.findall(r'(\d+)/(\d+)/(\d+)', text))

# Note that if you're going ot perform a lot of matching or searching, it
#  pays off to compile the pattern first. The module-level functions keep
#  a cache of recently compiled patterns, so there isn't a huge performance
#  hit, but you will save a few lookups and some extra processing by using
#  your own compiled pattern.
