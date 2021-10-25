def mult(a,b,prod=0):
    """
    a, b are nums. 
    DO NOT add an arg for prod - 
        it's there as a parameter so that prod = 0 can be declared before the function runs

    This function should 
    a. print the number of recursions remaining and the provisional product when it's still recursing
    b. RETURN the final product of ints a and b

    It's more verbose and inefficient than the best recursion prog for multiplication,
    but another approach doesn't hurt....right?
    """
    prod += a
    b -= 1
    print('Recursions left:', b, "| Product: ", prod)
    if b > 0:
        return mult(a,b,prod)
    else: 
        return prod
    
def mult2(a,b):
    """
    Dr. Grimson's recursion prog for multiplication in MIT 6.001x, Unit 4

    a, b are nums.
    The function should RETURN the product of a and b.
    """
    if b == 1:
        return a
    else:
        return a + mult(a,b-1)

print(mult(0.375,8))
