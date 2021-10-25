'''
INSTRUCTIONS:
Write a program to calculate the credit card balance after one year 
if a person only pays the minimum monthly payment (2%)
required by the credit card company each month.
'''

# Test Case 1:
balance = 42 # b -> balance (unpaid + paid)
annualInterestRate = 0.2 # r -> annual interest rate
monthlyPaymentRate = 0.04 # mp -> minimum rate of payment per month

# Submit the code below this line:
for i in range(12):
    # p(n)= mp * b
    # ub(n) = (b(n)-p(n))
    # b(n+1) = ub(n) + r/12.0 * ub(n)
    paymentMade = monthlyPaymentRate * balance
    unpaidBalance = balance - paymentMade
    balance = unpaidBalance + annualInterestRate/12.0 * unpaidBalance

# Be sure to print out no more than two decimal digits of accuracy (using round())
print('Remaining balance:', round(balance, 2))
