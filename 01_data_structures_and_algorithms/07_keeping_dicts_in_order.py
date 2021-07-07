# Problem
#  You want a dictionary and have control over the ordering
#   when iterating or serializing.

# Solution
#  You can use OrderedDict from collections module to control
#   the ordering of items. It preserves teh original insertion
#   order of data when iterating.
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])  # "foo 1", "bar 2", "spam 3", "grok 4"

#  An ordered dict can be useful when you need a mapping that
#   you may want to serialize or encode into a different format.
#  For example, if you want to control teh order of fields
#   appearing in JSON encoding, building the data in an OrderedDict
#   will do the trick.

import json
print(json.dump(d))  # '{"foo": 1, "bar": 2, "spam": 3, "grok": 4}'

# Discussion
#  An ordered dict internally maintains a doubly linked list that
#   orders the keys according to insertion order. When a new item
#   is inserted, it is placed at the end of the list. Reassigning
#   an existing key does not chagne the order.
#  The size of an OrderedDict is more than twice as large as a
#   normal dict due to the extra linked list that is created.
#  If you are going to build a data structure utilizing a large
#   number of ordered dict instances (reading 100,000 lines of
#   a CSV into a list of OrderedDict instances), you need to know
#   the requirements of you application to determine if the benefits
#   outweigh the memory overhead.
