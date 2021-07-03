# Problem
#  Need to unpack N items from an iterable
#  of length N + M where M > 0

# Solution
#  Use of the * operator to unpack into a list variable
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

record = ('Dave', 'dave@example.com', '773-424-4432', '843-956-0100')
name, email, *phone_numbers = record
print(name)  # 'Dave'
print(email)  # 'dave@example.com'
print(phone_numbers)  # [ '773-424-4432', '843-956-0100' ]

sales_record = [92.4, 93.1, 93.8, 89.9, 90.1, 90.7, 93.6, 98.7]
*trailing_qtrs, current_qtr = sales_record
print(trailing_qrts)  # [ 92.4, 93.1, 93.8, 89.9, 90.1, 90.7, 93.6 ]
print(current_qrt)  # 98.7

# Discussion
#  Extended iterable unpacking is useful when there are known
#  patterns in the data that is being handled. This way data
#  can be grouped in certain areas where needed. This is very
#  useful with handling a sequence of tuples of varying length
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

#  Star unpacking can also be useful with string
#  processing operations
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)  # 'nobody'
print(homedir)  # '/var/empty'
print(sh)  # '/usr/bin/false'

#  Star unpacking can also be used with throw away
#  variables
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)  # 'ACME'
print(year)  # 2012

#  There are similarities with star unpacking and list-
#  processing features.
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)  # 1
print(tail)  # [10, 7, 4, 5, 9]

# Extra Discussion
#  Star unpacking coudl be used to perform splitting in
#  recursive type algorithm/function. However, python
#  has an inherit recursive limit, so it isn't a strong
#  feature that is used often.
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))
