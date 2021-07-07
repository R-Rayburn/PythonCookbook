# Problem
#  You want to perform calculations on a dict of data.
# Solution
#  Consider a dict that maps stock names to prices
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

#  In order to perform useful calculations, it is
#   often useful to invert keys and values of the
#   dict using zip()

min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')

max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')

#  Similarly, you can rank data using zip() with sorted()

prices_sorted = sorted(zip(prices.values(), prices.keys()))
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
#                   (45.23, 'ACME'), (205.55, 'IBM'),
#                   (612.78, 'AAPL')]

#  When doing these calculations, know that zip() creates
#   an iterator that can only be consumed once

prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))
# print(max(prices_and_names))  # ValueError

# Discussion
#  If you try to perform data reductions on a dict, they
#   will only process the keys, not the values
min(prices)  # 'AAPL'
max(prices)  # 'IBM'

#  You might try to fix this by using the values() method
min(prices.values())  # 10.75
max(prices.values())  # 612.78

#  Unfortunately, this is usually not exactly what is needed.
#  You may want to know information about the corresponding keys.
#  You can get the key corresponding to the min or max value if
#   you supply a key function to min() and max()
min(prices, key=lambda k: prices[k])  # 'FB'
max(prices, key=lambda k: prices[k])  # 'AAPL'

#  To get the min value, you will need to perform an additional
#   lookup.
min_value = prices[min(prices, key=lambda k: prices[k])]

#  The solution with zip() solves the problem by "inverting" the
#   dict into a sequence of (value, key) pairs.
#  When performing comparisons on these tuples, the value element
#   is compared first, followed by the key.
#  This gives the requested behavior, allowing reductions and sorting
#   to be performed on the dict contents with a single statement.

#  Note that in calculations involving (value, key) pairs, the key
#   will be used to determine the reusult in instances wehre multiple
#   entries have the same value.
prices = {'AAA': 45.23, 'ZZZ': 45.23}
min(zip(prices.values(), prices.keys()))
# (45.23, 'AAA')
max(zip(prices.values(), prices.keys()))
# (45.23, 'ZZZ')

