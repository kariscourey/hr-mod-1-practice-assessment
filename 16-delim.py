# This function must take a string that is composed of values that are separated by some "delimiter" character, like a comma. It will return an array of the values in the string with the delimiter removed. Here is an example:

# input = "1,2,3,4"
# read_delimited(input)  # --> ["1","2","3","4"]
# If input is an empty string, the result should be a list with a single empty string in it : [""]

# Please refer to the split  method for strings to see how to do this.

# Please complete the read_delimited function here.



def read_delimited(line, separator=","):
    if line:
        return line.split(separator)

    return [""]


result = read_delimited("1,2,3,4")
print(result)
