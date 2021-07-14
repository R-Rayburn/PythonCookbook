# Problem
#  Need a list of largest or smallest N items in a collection

# Solution
#  heapq module has two functions that can do this.

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # [42, 37, 23]
print(heapq.nsmallest(3, nums))  # [-4, 1, 2]

#  Also contains a key parameter for complicated data structures

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

# Discussion
#  These functions are optimized for performance.
#  They work by converting the data into a list then a heap for ordering.

heap = list(nums)
heapq.heapify(nums)
print(heap)  # [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]

#  heap[0] is always the smallest item.
#  subsequent items can be found using heapq.heappop() method
#   this method pops off the first item and replaces it with the
#   next smallest item, a time complexity of O(logN)

#  Example of finding the three smallest items:
print(heapq.heappop(heap))  # -4
print(heapq.heappop(heap))  # 1
print(heapq.heappop(heap))  # 2

#  The nlargest() and nsmallest() funtions are most appropriate
#  for finding a small number of items. Finding a single smallest
#  item (N=1), min() or max() are faster. If N is about the same
#  size as the collection, then it is usually faster to sort it
#  and take the slice you need (sorted(items)[:N] or sorted(items)[-N:]).
#  The two heapq functions are adaptive and optimized to these implementations,
#  like using sorting if N is close to the size of the items.
