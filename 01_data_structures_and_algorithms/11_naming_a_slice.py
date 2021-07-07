# Problem
#  Your program is unreadable due to hardcoded slice
#   indices.

# Solution
#  Suppose you have code to pull specific data fields
#   out of a string with fixed fields.

#####     0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.25     ..........'
cost = int(record[20:32]) * float(record[40:48])

#  Instead of having the hardcoded slices, store them in variables

SHARES = slice(20,32)
PRICE  = slice(40,48)

cost = int(record[SHARES]) * float(record[PRICE])

#  The latter version avoids having a lot of mystery with hardcoded
#   indices, and the code becomes much clearer

# Discussion
#  Writing code with a lot of hardcoded index values leads to a
#   readability and maintenance mess.
#  The built in slice() creates a slice object that can be used anywhere
#   a slice is allowed

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])  # [2, 3]
print(items[a])    # [2, 3]
items[a] = [10,11]
print(items)  # [0, 1, 10, 11, 4, 5, 6]
del items[a]
print(items)  # [0, 1, 4, 5, 6]

#  If you have a slice instance s, you can get more info about it by
#   looking at the s.start, s.stop, s.step attributes
a = slice(5, 50, 2)
print(a.start)  # 5
print(a.stop)   # 50
print(a.step)   # 2

#  You can map a slice onto a sequence of a specific size by using
#   indices(size) method.
#  This returns a tuple (start, stop, step) where all values have been
#   limited to fit wihtin bounds.
#  This avoids IndexError exceptions when indexing.

s = 'HelloWorld'
print(a.indices(len(s)))  # (5, 10, 2)
for i in range(*a.indices(len(s))):
    print(s[i])  # W, r, d
