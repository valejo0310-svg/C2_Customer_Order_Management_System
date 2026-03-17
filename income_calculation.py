# A function will be created that will sum all the totals of the registered orders.

def income_calculation(order):

    # A variable is created where the total sum of the income will be stored.
    total_income = 0

    # Here we will iterate through what is stored in the dictionary value where the calculation of the total_order variable is saved.
    for order_id in order:

        # Everything stored in the dictionary is added together with the value "total".
        total_income += order[order_id]["total"]
    
    # The entire sum is returned.
    return total_income