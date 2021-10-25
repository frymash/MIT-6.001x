import time

cube = int(input("Number: "))
epsilon = 0.01
# this epsilon is necessary in order to ensure the guess is as close to 0 
# as possible. however, it must be set properly in accordance with the 
# increment to prevent infinite guessing.
guess = 0.0
increment = 0.0001
num_guesses = 0

while abs(guess**3 - cube) >= epsilon and guess <= cube:
    print(abs(guess**3 - cube), "Guess:", guess)
    guess += increment
    num_guesses += 1
    # time.sleep(0.02)

print('num_guesses', num_guesses)

if abs(guess**3 - cube) >= epsilon:
    print("Failed to evaluate cube root of ", cube)
else:
    print(guess, "is close to the cube root of", cube)
