#!/usr/local/bin/python3

# g is a Number (int or float)
# interp. the guess for a square root number
# examples: g = 2, g = 4.5
# def fn-for-g(g: float) -> Any:
#   (... g)

from typing import Union

print("--- USING NEWTON'S METHOD TO APPROXIMATE SQUARE ROOTS---")

def newton(k: Union[int,float], g: Union[int,float], e: float = 0.01) -> None:
    """ Approximates the square root of a number k by using Newton's method
    with initial guess g and epsilon e

    Examples:
        newton(81, 40.5, 0.01) # Answer: 9
        newton(225, 112.5, 0.01) # Answer: 15
    """

    num_guesses = 0

    while abs(g**2 - k) >= e and g <= k:
        print(f"{abs(g**2 - k)} | Guess: {g} | No. of guesses: {num_guesses}")
        g = g - ((g**2-k)/(2*g))
        num_guesses += 1

    if abs(g**2 - k) >= e:
        print("Failed to calculate square root. Please try again.")

    else:
        print(f"{g} is close to the square root of {k}.")

k = float(input("Enter the number whose square root is to be guessed: "))

newton(k, k/2, 0.01)
