# Problem
#  Want to keep the last few items during processing

# Solution
#  Keeping limited history is prefect fo rcollactions.deque

from collections import deque

#  Performs a text match on sequence of lines and yields the matching
#   line along with the previous N lines
#  This is an example of a generator function that seems to return two
#   objects, but actually returns a generator (an iterator) that can be
#   iterated over.
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)

# Discussion
#  It is commen to use a generator funciton when writing code to
#   search for items. This helps with decoupling the searching
#   process from the code that utilizes the results.
#  deque(maxlen=N) creates N-sized queue. When new items are
#   added and the queue is full, then the oldest item is removed

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)  # deque([1, 2, 3], maxlen=3)
q.append(4)
print(q)  # deque([2, 3, 4], maxlen=3)
q.append(5)
print(q)  # deque([3, 4, 5], maxlen=3)

#  When not giving it a maximum size, an unbounded queue is
#   created, letting you append on either end.

q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)  # deque([1, 2, 3])
q.appendleft(4)
print(q)  # deque([4, 1, 2, 3])
print(q.pop())  # 3
print(q)  # deque([4, 1, 2])
print(q.popleft())  # 4

#  Adding or popping from the ends of a queue is O(1) complexity
