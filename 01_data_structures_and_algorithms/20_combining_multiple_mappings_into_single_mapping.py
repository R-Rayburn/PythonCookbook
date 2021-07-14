# Problem
# There are multiple dicts/maps that you want to logically combine into a single
#  mapping ot perform certain operations, like looking up values or checking for
#  keys.

# Solution
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# Suppose you want to perform lookups on both dicts (checking a then be if not in a).
# This can be done using the ChainMap class from the collections module.
from collections import ChainMap
c = ChainMap(a,b)
print(c['x'])  # 1 (from a)
print(c['y'])  # 2 (from b)
print(c['z'])  # 3 (from a)

# Discussion
# ChainMap takes multiple mappings and makes them appear as one.
# These mappings are not literally merged together.
# A ChanMap simply keeps a list of teh underlying mappings and redefines
#  common dict operations to scan a list.
print(len(c))  # 3
print(list(c.keys()))  # ['x', 'y', 'z']
print(list(c.values()))  # [1, 2, 3]

# If there are duplicate keys, the values from the first mapping get used.
# Thus c['z'] in the example would always refer to the value in dict a, not dict b.

# Operations taht mutate the mapping affect teh first mapping listed.
import traceback
c['z'] = 10
c['w'] = 40
del c['x']
print(a)  # {'w':40, 'z':10}
try:
    del c['y']  # KeyError
except Exception:
    traceback.print_exc()

# A ChanMap is useful when working with scoped values such as variables
#  in programming languages (globals, locals, etc)

values = ChainMap()
values['x'] = 1
# Add new mapping
values = values.new_child()
values['x'] = 2
# Add new mapping
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])  # 3
# Discard last mapping
values = values.parents
print(values['x'])  # 2
# Discard last mapping
values = values.parents
print(values['x'])  # 1
print(values)

# An alternative to ChanMap is merging dictionaries together using update()
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

merged = dict(b)
merged.update(a)
print(merged['x'])  # 1
print(merged['y'])  # 2
print(merged['z'])  # 3

# This requires you to make a separate dict object (or destructively alter an existing dict).
# Also, mutations on original dicts don't get reflected in the merged dict.
a['x'] = 13
print(merged['x'])  # 1

# A ChainMap uses the original dicts, so it doesn't have this behavior
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
print(merged['x'])  # 1
a['x'] = 42
print(merged['x'])  # 42
