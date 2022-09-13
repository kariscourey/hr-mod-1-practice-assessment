# This function takes a list of strings and returns the longest string in the list.

# Note: The input data will have only one longest string.

# Here are some examples:

# strings	output
# []	None
# ["a"]	"a"
# ["a", "bbb", "cc"]	"bbb"
# Think through this problem. It may seem complex, but you can do this.

# What gets returned for an empty list?
# Can you do this with a single if statement?
# Can you do this with a for loop?

def find_longest(strings):
    if strings:
        return max(strings, key=len)

val = ["a", "bbb", "cc"]
print(find_longest(val))
