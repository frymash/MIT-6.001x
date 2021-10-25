# Test case 3 (Answer= 360)
balance = 3926
annualInterestRate = 0.2

# Submit code below this line
x = 0
initialBalance = balance

while balance > 0:
	x +=10
	balance = initialBalance
	
	for n in range(12):
		unpaidBalance = balance -x
		balance = unpaidBalance + (annualInterestRate/12.0 * unpaidBalance)

print('Lowest payment:', x)
