# Problem
#  You have a sequence of items you want to iterate over in groups based on a field
#   value.

# Solution
#  The itertools.groupby() function is useful for grouping data together.

rows = [
    {'address':'5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('\t', i['address'])

# Discussion
#  groupby() works by cannign and finding sequential "runs" of identical values in a sequence.
#  On each iteration, it returns the value along with an iterator that contains the grouped items.
#  It is important to sort the data according to the field to group by. This is because groupby()
#   only examines consecutive items. Failure to sort will not properly group records.
#  If you are wanting to simply group data in a large data structure that allows random access,
#   you may have better luck using defaultdict() to build a multidict

from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
    print(r)

#  This might be preferred if memory if of no concern, and you want the
#   code to possibly run faster.
