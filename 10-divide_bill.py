# Implement the function divide_bill which will return the amount due for each diner given: a total bill, number of diners, and the desired tip amount.

def divide_bill(bill, num_diners, tip=0.2):
    return bill * (1+tip) / num_diners


print(divide_bill(30,4,0.1))
