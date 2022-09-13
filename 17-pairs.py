# Please complete the pair_up function below so that it takes a list of items and returns a list of pairs of consecutive items. Here's an example:

# input = [1,2,3,4,5,6,7]

# pair_up(input)  # Returns [[1,2], [3,4], [5,6]]
# Note: since there were an odd number of items, the 7 didn't have a partner to pair with, so it was excluded

# Think through this problem. It may seem complex, but you can do this.

# What gets returned for an empty list?
# Can you do this with a single if statement?
# Can you do this with a for loop?

def pair_up(items):

    # paired = []
    # result = []

    if items:

        # while len(paired) < 2:
        #     for i in items:
        #         paired.append(i)
        #     result.append(paired)
        #     paired = []

        result = [items[i:i+2] for i in range(0,len(items),2)]

        last = result[-1]
        if len(last) == 1:
            result.pop()

        return result

    return []

# def pair_up(items):
#     return [[items[i], items[i+1]] for i in range(len(items)-1)][0::2]


print(pair_up([1,2,3,4,5,6,7]))
print(pair_up([]))
