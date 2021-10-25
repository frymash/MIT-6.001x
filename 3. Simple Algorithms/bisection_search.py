#!/usr/bin/env python3

# Bisection search to find sqrt(x)

print("--- BISECTION/BINARY SEARCH ALGO TO FIND SQUARE ROOTS OF A NUMBER ---")
x = int(input("Pick a number: "))
epsilon = 0.01
num_guesses = 0
low = 1
high = x
# Let the guess be g, 
g = (low + high) / 2.0

while abs(g**2 - x) >= epsilon:
    num_guesses += 1
    print("No. of guesses made: ", num_guesses, "| Guess: ", g)
    if g**2 > x:
        high = g
    else:
        low = g
    g = (low + high) / 2.0

print(g, "is close to the square root of", x)
print(num_guesses, "guesses were made")
    