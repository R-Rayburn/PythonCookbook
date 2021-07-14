# Problem
# You have a sequence of data that you would like to extract values from or reduce based on criteria.

# Solution
# The easiest way to filter sequence data is often using list comprehension
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])  # [1, 4, 10, 2, 3]
print([n for n in mylist if n < 0])  # [-5, -7, -1]

# One downside of list comprehension is it might produce large results.
# This can be resolved by using generator expressions to produce the values iteratively.
pos = (n for n in mylist if n > 0)
print(pos)
for x in pos:
    print(x)

# Sometimes list or generator expression doesn't easily express teh filtering criteria.
# An example is that the process involved exception handling or other complicated detail.
# To resolve this, you can put the filtering code into a function and use the built-in
#  filter() function.
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)  # ['1', '2', '-3', '4', '5']

# filter() creates an iterator, so you will want to use list() to convert the results if
#  a list is what you want.

# Discussion
# List comprehensions and generator expressions are often the best ways to filter simple data.
# They can also transform the data at the same time.
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math
print([math.sqrt(n) for n in mylist if n > 0])

# A variation of filtering is replacing values that don't meet criteria with a new value.
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)  # [1, 4, 0, 10, 0, 2, 3, 0]
clip_pos = [n in n < 0 else 0 for n in mylist]
print(clip_pos)  # [0, 0, -5, 0, -7, 0, 0, -1]

# Another filtering tool is itertools.compress(). This takes an iterable and accompanying
# Boolean selector sequence as input. It gives all the items in the iterable where the
# corresponding element in the selector is True. This is useful if you want to apply results
# of filtering one sequence to a parallel/related sequence.
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

# list of addresses where count value is greater than 5
from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)  # [False, False, True, False
print(list(compress(addresses, more5)))  # ['5800 E 58TH', '4801 N BROADWAY', '1039 W GRANVILLE']

# The key is to create a sequence of bools to indicate which element satisfies the codition.
# compress() then selects teh items corresponding to True values.
# compress() returns an iterator, thus it needs to be converted to a list if that is what is desired.
