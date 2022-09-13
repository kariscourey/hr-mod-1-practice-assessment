# Implement the function add_all() which returns the sum of all of its arguments.

# Sample inputs/outputs

# The numbers parameter will contain a list
# of numbers for you to add together
def add_all(*numbers):
    return sum(numbers)


numbers=[1,2,3]
print(add_all(numbers))
