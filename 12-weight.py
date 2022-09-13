# This function takes a list of items in a shipment and calculates the total weight of the shipment. Below is an example shipment list in Python:

# shipment = [
#     {
#         "product_name": "can of soup",
#         "product_weight_pounds": 3.4,
#         "quantity": 3,
#     },
# ]
# The total weight for the example above would be 3 x 3.4 = 10.2.

# Here's an example with two items:

# shipment = [
#     {
#         "product_name": "beans",
#         "product_weight_pounds": 2,
#         "quantity": 5,
#     },
#     {
#         "product_name": "rice",
#         "product_weight_pounds": 1.5,
#         "quantity": 7,
#     },
# ]
# The total weight for this shipment is: (2 x 5) + (1.5 x 7) = 20.5

# If the shipment list is empty, then the function should return 0.

# Think through this problem. It may seem complex, but you can do this.

# What gets returned for an empty list?
# Can you do this with a single if statement?
# Can you do this with a for loop?

def find_shipment_weight(shipment):

    sum = 0

    if shipment:
        for i in shipment:
            sum += i.get("product_weight_pounds") * i.get("quantity")

    return sum
