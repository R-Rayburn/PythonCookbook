# Problem
#  You have a sequence of items that you want to find the most frequently
#   occurring items.

# Solution
#  collections.Counter class is designed for this problem.
#  It has a most_common() method that will give you the answer you want.

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)  # [('eyes', 8), ('the', 5), ('look', 4)]

# Discussion
#  Counter objects can be fed any sequence of hashable items.
#  A Counter is a dictionary that maps the items to the number of occurrences.

print(word_counts['not'])  # 1
print(word_counts['eyes'])  # 8

#  You can increment the count manually using addition
more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in more_words:
    word_counts[word] += 1

print(word_counts['eyes'])  # 9

#  You can also do this by using the update() method
word_counts.update(more_words)

#  Counter instances can be combined using various mathematical operations.
a = Counter(words)
b = Counter(more_words)
print(a)
print(b)
# Combine counts
c = a + b
print(c)
# Subtract counts
d = a - b
print(d)

#  Counter objects are useful tools for tabulating
#   and counting data. This should be used over
#   over manually written solutions using dicts.
