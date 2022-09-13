# The function below takes a list of items and returns a copy of the list with all of the duplicate items removed in the same order that they were encountered in the list.

# Examples:

# input	output
# []	[]
# [1,2]	[1,2]
# [1,1,2]	[1,2]
# [1,2,1]	[1,2]
# [2,1,1]	[2,1]
# [1,1,1]	[1]

def unique_elements(items):

    # output = []

    # for i in items:
    #     if i not in output:
    #         output.append(i)
    # return output

    uniques = {}
    for i in items:
        uniques[i] = 1
    return list(uniques.keys())


result = unique_elements([1,1,1,2,3,4,4,5])
print(result)
