# This function returns True if number is an integer multiple of base where number and base are both integers. If base is an integer multiple of number, then number/base is an integer.

# Here are some examples:

# number	base	output	reason
# 6	1.5	False	1.5 is not an integer
# 6	2	True	6 is a multiple of 2
# 6	3	True	6 is a multiple of 3
# 6	4	False	6 is not a multiple of 4
# You can test if the number in a variable is an integer by using the int function to turn the value into an integer, then seeing if it equals the original value, like this.

# if int(x) == x:
#     # Then, x is an integer
# You can use the modulo operator % to check to see what the remainder of division is. If the remainder is 0, then the second number evenly divides the first number.

# x = 10
# y = 2
# print(x % y)  # Prints 0

# x = 10
# y = 3
# print(x % y)  # Prints 1

# x = 10
# y = 4
# print(x % y)  # Prints 2

# x = 10
# y = 5
# print(x % y)  # Prints 0

def is_multiple_of(number, base):
    return (isinstance(base, int)) and (number % base == 0)


print(is_multiple_of(6,2))
print(is_multiple_of(6,1.5))
