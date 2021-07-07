# Problem
#  Need a dictionary that maps keys ot more than one value (multidict)
# Solution
#  To store multiple values with a single key, a container such as a
#   list or set should be used.
d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

#  Lists are useful when wanting to maintain insertion order,
#   sets are useful to eliminate duplicates.
#  These dictionaries can be created by using defaultdict in
#   the collections module. defaultdict automatically
#   initializes the first value so that the focus can be on
#   adding items to the dict.
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

#  defaultdict will automatically create dictionary entities for keys
#   accessed later on (even if those keys don't currently exist in
#   the dict). If this behavior isn't wanted, then the setdefault()
#   method for an ordinary dict can be used.

d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).appemd(4)

#  Many find setdefault() to be unnatural, and it always creates
#   a new instance of the initial value on each invocation (the
#   empty list [] in the example above)

# Discussion
#  Consturcting a multivalued dict is simple in principle, but
#   initializing the first value can be messy.

d = {}
pairs = [
    ('a', 1),
    ('a', 2),
    ('b', 4)
]
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

#  Using defaultdict() simplifies the code
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)

#  This recipe is related to the problem with needing to group
#   records in data processing problems. 01.15 is an example of
#   this.
