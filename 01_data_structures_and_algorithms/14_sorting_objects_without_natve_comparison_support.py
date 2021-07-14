# Problem
#  You need to sort objects of the same class, but they don't natively support comparison operations.

# Solution
#  The built in sorted() function takes a key argument that can be passed a callable that will return some values in the object that the sorted function will use to compare the objects.
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
print(users)
print(sorted(users, key=lambda u: u.user_id))

#  An alternative to using lambda is using operator.attrgetter()

from operator import attrgetter
print(sorted(users, key=attrgetter('user_id')))

# Discussion
#  The choice over lambda or attrgetter is a matter of personal preference. Like itemgetter(), attrgetter() often runs faster than lambdas, and has the added feature of allowing multiple fields to be extracted simultaneously (see recipe 01.13).

class User:
    def __init__(self, first, last):
        self.fname = first
        self.lname = last
    def __repr__(self):
        return f'{self.fname} {self.lname}'

avengers = [
    User('Peter', 'Parker'),
    User('Tony', 'Stark'),
    User('Bruce', 'Banner'),
    User('Thor', 'Odenson'),
    User('Loki', 'Odenson')
]

by_name = sorted(avengers, key=attrgetter('lname', 'fname'))
print(by_name)

print(min(users, key=attrgetter('user_id')))
print(max(users, key=attrgetter('user_id')))
