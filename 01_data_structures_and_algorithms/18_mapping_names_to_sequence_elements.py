# Problem
# You have code to access list or tuple elements by position, but the code is
#  difficult to read at times.
# You would like to be less dependent on position by accessing the elements
#  by name.

# Solution
# collections.namedtuple() privides what we want, while adding minimal overhead.
# collections.namedtuple() is a factory method that returns a subclass of the
#  tuple type.
# You give it a type name, and the fields it should have, and it returns a class
#  that you can instantiate, passing in values for the fields and so on.
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2021-10-19')
print(sub)  # Subscriber(addr='jonesy@example.com', joined='2021-10-19')
print(sub.addr)  # 'jonesy@example.com'
print(sub.joined)  # '2021-10-19'

# Although an instance of namedtuple looks like a class instance, it is interchangeable
#  with a tuple and supports all usual tuple operations like indexing and unpacking
print(len(sub))  # 2
addr, joined = sub
print(addr)  # 'jonesy@example.com'
print(joined)  # '2021-10-19'

# A use case for this is decoupling code from the position of the elements it manipulates.
# So if you get a large list of tuples from a db call, then manipulate them by accessing
#  positional elements, the code could break if a new column was added to the table.
# This doesn't happen if you cast the returned tuples to namedtuples

def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

# The above example shows code that is less expressive and more dependent on the structure
#  of records, due to the positional references to the elements.

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

# You can avoid the explicit conversion to Stock if the records
#  sequence in the above example already contained such instances.

# Discussion
# A use for namedtuple is as a replacement for a dict, which requires more storage space.
# If building large data structures, namedtuple will be more efficient than a dict.
# However, a namedtuple is immutable, unlike a dict
import traceback
s = Stock('ACME', 100, 123.45)
print(s)  # Stock(name='ACME', shares=100, price=123.45)
try:
    s.shares = 75  # AttributeError
except Exception:
    traceback.print_exc()

# If you need to change attributes, it can be done using _replace() method.
# This makes a new namedtuple with specified values replaced.
s = s._replace(shares=75)
print(s)  # Stock(name='ACME', shares=75, price=123.45)

# A subtle use for _replace() is taht it can be a useful way to populate
#  named tuples that have optional or missing fields.
# To do this, create a prototype tuple containing default fields, then use
#  replace() to create new instances with values replaced.
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# prototype
stock_prototype = Stock('', 0, 0.0, None, None)

# Converts dict to Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))  # Stock(name='ACME', shares=100, price=123.45, date=None, time=None)
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/12/2021'}
print(dict_to_stock(b))  # Stock(name='ACME', shares=100, price=123.45, date='12/12/2021', time=None)

# Note that if your goal is to define an efficient data structure where you will be changing various
#  instance attributes, namedtuple is not the best choice.
# Consider defining a class using __slots__ instead (Recipe 08.04)
