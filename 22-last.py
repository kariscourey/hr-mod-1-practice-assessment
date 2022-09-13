# There are a couple of problems with the last_item function.

# It is supposed to return the last item of the list passed in through the list parameter
# If the list parameter contains an empty list, then it should return None
# Update the code below so that it passes its unit tests

def last_item(list):
    if list:
        # last_item = list[len(list) - 1]
        last_item = list[-1]
        return last_item
