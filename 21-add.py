# This function works when items only has strings in it, but fails if there are any non-string things.

# The function should make sure that each item in items is converted to a string before concatenating it to the result.

# Fix the code below to handle non-string items.

def join(items):
    result = ""
    for item in items:
        result += str(item)
    return result
