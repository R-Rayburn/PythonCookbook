# Problem
#  You would like to sort a list of dicts according
#   to one or more of the dicts' values.

# Solution
#  This can be done using the operator module's itemgetter
#   function.
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

# Sort by first name
rows_by_fname = sorted(rows, key=itemgetter('fname'))
# Sort by user id
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

# Sort by last name, then first name
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

# Discussion
#  The key argument is expected to be a callable that accepts a single item from the enumerable as input and returns a value that will be used as the basis for sorting. itemgetter() creates this callable. The operator.itemgetter() functiontakes as arguments the lookup indices used to extract the desired values from the records in the enumerable. It can be a dict key name, a numeric list element, or any value that can be fed to an object's __getitem__() method. When multiple indices to are given to itemgetter(), the callable witll retun a tuple with the items in it, an dsorted will order the output according to the sorted order of the tuples. This is useful when wanting to sort on multiple fields. The functionality of itemgetter() is sometimes replaced by lambda expressions

rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, keys=lambda r: (r['lname'], r['fname']))

#  This solution works identically, however, the itemgetter() version typically runs a bit faster, and might be preferred if performance is a concern.
#  These techniques can be applied to functions like min() and max() or other similar functions
print(min(rows, key=itemgetter('uid')))  # record with uid 1001
print(max(rows, key=itemgetter('uid')))  # record with uid 1004
