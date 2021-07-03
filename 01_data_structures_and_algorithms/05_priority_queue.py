# Problem
#  Need a queue that sorts items by priority that
#   always returns the item with highest priority
#   on each pop.

# Solution

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())  # Item('bar')
print(q.pop())  # Item('spam')
print(q.pop())  # Item('foo')
print(q.pop())  # Item('grok')

#  The first pop returned the item with the
#   highest priority, and the two items with
#   the same priority are returned in the
#   order they were inserted into the queue

# Discussion
#  This recipe utilizes the heapq module.
#  The functions heapq.heap() and heapq.heappop()
#   insert and remove items to _queue where teh first
#   item in the list is the smallest priority (04).
#  Since heappop() always returns the smallest item,
#   it is the key to making the queue pop teh correct
#   items. Since push and pop have O(logN) complexity,
#   where N is the size of the queue, it is pretty
#   efficient.
#  In this instance, the queue contains tuples of
#   (-priority, index, item). The priority value is
#   negated in order to sort the items from hightest
#   priority to lowest priority in the queue. This is
#   opposite of the normal heap ordering, which sorts
#   low to high (the reason for negation)
#  The index variable is used to properly order items
#   with the same priority level. The items will be
#   sorted according to the order it was inserted due
#   to the continuously incrementing variable. However,
#   the index makes the comparison operations work for
#   items of the same priority level.

# These Items cannot be ordered
a = Item('foo')
b = Item('bar')
# a < b  # throws TypeError

#  If you have (priority, item) tuples, they can be
#   compared as long as the priorities are different.
#  If two tuples have equal priority, the comparison
#   falls on the second item and fails like above
a = (1, Item('foo'))
b = (5, Item('bar'))
print(a < b)  # True
c = (1, Item('grok'))
# a < c  # throws TypeError

#  Creating an extra index by making (priority, index, item)
#   tuples avoids this problem, since no two tuples will
#   ever have the same value for index (and Python never
#   bothers to compare the remaining tuple values.
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
print(a < b)  # True => based on priority
print(a < c)  # True => based on index

# If this queue was to be used for communication between threads,
#  appropriate locking and signaling would need to be added. This
#  will pop up in 12.03
