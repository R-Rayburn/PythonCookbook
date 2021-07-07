# Problem
#  You have two dicts that you want to know what they
#   have in common

# Solution

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

#  To find what a and b have in common, perform
#   set operations on keys() or items() methods

# Find keys in common
a.keys() & b.keys()  # {'x', 'y'}

# Find keys in a that are not in b
a.keys() - b.keys()  # {'z'}

# Find (key,value) pairs in common
a.items() & b.items()  # { ('y', 2) }

#  These operations can also alter or filter dicts.
#  Suppose you want a new dict with selected keys removed

# Making a dict with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}

# Discussion
#  The keys() method of a dict returns a keys-view
#   object that exposes the keys.
#  Keys views supports common set operations like
#   unions, intersections, and differences.
#  If you need to perform set operations with dict
#   keys, you can often just use the keys-view
#   objects directly without converting them into a set.
#  The items() method returns an items-view consiting of
#   (key, value) pairs.
#  This object supports set operations and can be used
#   to perform operations such as finding out which
#   key-value pairs two dicts have in common
#  The values() method of a dictionary does not support
#   set operations, due to the fact that items in the
#   values view are not guaranteed to be unique.
#  This makes certain set operations questionable utility
#   with values() content.
#  If set operations need to be performed, the values
#   can be converted to a set before the operations are performed.
