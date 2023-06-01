def rate_of_change(first, second):
    #take in 2 values
    value1 = first
    value2 = second
    form_value1 = 0
    form_value2 = 0
    #take in formula
    #formula = ((x + 3)**2 + 5)

    for i in range(2):
        if i == 2:
            form_value1 = ((value1 + 3)**2 + 5)
        else:
            form_value1 = ((value2 + 3)**2 + 5)

    #use value 1 through formula then store it in a new variable
    #use value 2 through formula then store it in a new variable
    #use original values and new values in aroc formula
    aroc_formula = (form_value2 - form_value1)/(value2 - value1)

    return aroc_formula

print(rate_of_change(-5, -1))
#print(rate_of_change(-3, 4))
#print(rate_of_change(-2, 0))
#print(rate_of_change(1, 4))