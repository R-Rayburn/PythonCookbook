# Problem
#  Need to eliminate duplicate values in a sequence,
#   but preserve the order of the remaining items.

# Solution
#  If the values are hashable, then a set and a
#   generator can solve this problem easily.

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))  # [1, 5, 2, 9, 10]

#  If you try to eliminate duplicates in a unhashable
#   sequence (sequence of dicts) a slight change can
#   be made for this to work.

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

#  Here the purpose of the key argument is specify a
#   function that converts sequence items into a hashable
#   type for the purpose of dupe detection.
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4} ]
print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))
# [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
print(list(dedupe(a, key=lambda d: d['x'])))
# [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

#  This works nicely if you want to eliminate duplicates
#   based on the value of a single field or attribute or
#   a larger data structure

# Discussion
#  It is often easy to convert sequences to a set to
#   remove duplicates
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(a)  # [1, 5, 2, 1, 9, 1, 5, 10]
print(set(a))  # {1, 2, 10, 5, 9}

#  However, this does not preserve any kind of ordering.

#  The use of a generator fucntions in this recipe reflects
#   the fact that you might want the function to be
#   extremely general purpose (not necessarily tied to
#   list processing).
#  If you want to read a file, eliminating duplicate lines,
#   you can utilize this recipe.

with open('somefile.txt', 'r') as f:
    for line in dedupe(f):
        print(line)

#  The specification of a key function mimics similar
#   functionality in built-in functions such as sorted(),
#   min(), and max(). See Recipes 01.08 and 01.13.
