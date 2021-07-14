# Problem
# A reduction function needs to be ran on datat that needs
#  to be filtered or transformed first.

# Solution
# An eligant way ot combine these is to use a generator-expression argument
nums = [1, 2, 3, 4, 5]
# Sums of squares
s = sum(x * x for x in nums)
print(s)

# Determines if python files exist in dir
import os
files = os.listdir('./')
if any(name.endswith('.py') for name in files):
    print('There by python!')
else:
    print('Sorry, no python.')

# Outputs a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data struct
portfolio = [
    {'name':'GOOG', 'shares':50},
    {'name':'YHOO', 'shares':75},
    {'name':'AOL' , 'shares':20},
    {'name':'SCOX', 'shares':65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

# Discussion
# The solutions above shows a subtle syntactic aspect of generator
#  expressions wiht supplying a single argument.
# These are teh same:
s = sum((x * x for x in nums))  # passes generator-expr as argument
s = sum(x * x for x in nums)    # more elegant syntax

# Useing a generator argument is often more efficient and elegant than
#  crating a temp list.
nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])

# The above example works, but it provides an extra step that creates an
#  extra list.
# This might not matter for small lists, but larger lists will create larger
#  temp data structures that will be used once then discarded.
# The generator solution transforms the data iteratively, making it more
#  memory-efficient.

# Reduction functions that accept a key argument might be useful in situations
#  where you are inclined to use a generator.

# Original: Returns 20
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares)
