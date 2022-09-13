# The join_strings returns a single string that is the concatenation of all of the input strings, separated by the separator if supplied. Example:

# join_strings(["aaa", "bbb", "ccc"], "--")
#     # Returns "aaa--bbb--ccc"
# Think through this problem. It may seem complex, but you can do this.

# What gets returned for an empty list?
# Can you do this with a single if statement?
# Can you do this with a for loop?

def join_strings(strings, separator=""):

    result = []

    for i in strings:
        result.append(i)
        if strings.index(i) != len(strings) - 1:
            result.append(separator)

    return "".join(result)


print(join_strings(["aaa", "bbb", "ccc"], "--"))
