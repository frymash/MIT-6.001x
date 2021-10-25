# import time

# Test case 1 (Answer = 29157.09)
balance = 320000
annualInterestRate = 0.2

# Submit code below this line
# Let x be the payment per month and
# let r be the monthly interest rate,
r = annualInterestRate /12.0
low = balance / 12
high = (balance *((1+r)**12))/12.0
initialBalance = balance

while True:
	x = (low + high)/2
	balance = initialBalance
	
	for n in range(12):
			unpaidBalance = balance -x
			balance = unpaidBalance + (r * unpaidBalance)
			
	# For debugging:		
	# print('Payment amount:', x)
	# print('Low:', low, '| High:', high)
	# print('Balance: ', balance)
			
	if abs(balance) < 0.01:
		break
	elif balance > 0: # x is too low
		low = x
	elif balance < 0: # x is too high
		high = x
	# time.sleep(0.3)

print('Lowest payment:', round(x,2))
