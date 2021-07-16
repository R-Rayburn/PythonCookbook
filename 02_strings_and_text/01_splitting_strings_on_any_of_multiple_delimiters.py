# Problem
# A string needs to be split into fields, but the delimiters aren't consistent throughout the string.

# Solution
# split() is meant for simple cases and doesn't allow for multiple delimiters or account for whitespace around delimiters.
# re.split() will give more flexibility in this case.
line = 'asdf fjdk; afed, fjek,asdf,       foo'
import re
# Output: ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
print(re.split(r'[;,\s]\s*', line))

# Discussion
# re.split() is useful because multiple patterns for the separator can be specified.
# In the solution above, the separator is either a comma (,), semicolon (;), or whitespace
#  followed by any amount of extra whitespace.

# When using re.split(), you need to be careful should the regular expression pattern involve a capture
#  group enclosed in parentheses.
# If capture groups are used, then the matched text is also included in the result.
fields = re.split(r'(;|,|\s)\s*', line)
# Output: ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
print(fields)

# Getting the split characters might be useful for certain contexts, like reforming an output string
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)
# Reform teh line using the same delimiters
print(''.join(v+d for v,d in zip(values, delimiters)))

# If you don't want the separator characters in the results, but still need the parentheses
#  to group parts of the RegEx, make sure to use a noncapture groupe, (?:...)
print(re.split(r'(?:,|;|\s)\s*', line))
