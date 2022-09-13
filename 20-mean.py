# The following function is failing the unit tests with a divide by zero error when called like this:

# numbers = []
# mean(numbers) # --> ZeroDivisionError: division by zero
# If this situation is detected, It should return float('nan').

# Update the code below to handle this situation and pass the failing unit test.

def mean(numbers):
    try:
        total = sum(numbers)
        return  total / len(numbers)
    except ZeroDivisionError:
        return float('nan')
