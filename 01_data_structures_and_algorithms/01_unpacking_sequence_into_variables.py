# Problem:
#  Need to unpack N-element tuple or sequence
#  into N variables

# Solution:
p = (4, 5)
x, y = p
print(x)  # 4
print(y)  # 5
print()

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
print(name)  # 'ACME'
print(date)  # (2012, 12, 21)
name, shares, price, (year, mon, day) = data
print(name)  # 'ACME'
print(year)  # 2012
print(mon)  # 12
print(day)  # 21
print('\n')

# p = (4, 5)
# x, y, z = p  # Throws error due ot mismatch in unpacking


# Discussion
#  Unpacking works with any iterable
s = 'Hello'
a, b, c, d, e = s
print(a)  # 'H'
print(b)  # 'e'
print(e)  # 'o'
print('\n')

#  When unpacking you can also discard variable
#  using _ or your choice of throwaway variable
#  NOTE: if you choose to use a custom throwaway
#        variable, make sure it is not in use.
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ = data
print(shares)  # 50
print(price)  # 91.1
