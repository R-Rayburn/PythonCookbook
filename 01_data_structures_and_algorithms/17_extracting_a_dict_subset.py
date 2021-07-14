# Problem
# Want a dictionary that is a subset of another dictionary
# Solution
# dictionary comprehension
prices = {
    'ACME':  45.23,
    'AAPL': 612.78,
    'IBM':  205.55,
    'HPQ':   37.20,
    'FB':    10.75
}

# Prices above 200
p1 = { key:value for key, value in prices.items() if value > 200 }
print(p1)

# tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = { key:value for key, value in prices.items() if key in tech_names }
print(p2)

# Discussion
# This can be done with creating a sequence of tuples and utilizing the dict() funciton

p1 = dict((key,value) for key, value in prices.items() if value > 200)
print(p1)

# However, the dict comp solution is a bit clearer and a bit faster

# There are multiple ways to do the dict comp.
p2 =  { key:prices[key] for key in prices.keys() & tech_names }

# A study on this reveiled that the above solution is 1.6 times slower than the first
#  one that was given. If performance matters, it pays to spend a bit of time studying
#  different implementations. Recipe 14.13 has info on timing and profiling.
