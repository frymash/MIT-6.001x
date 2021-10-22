print("Please think of a number between 0 and 100! ")
low = 0
high = 100

while True:
    # Let the guess be g,
    g = (low + high) // 2
    print("Is your secret number", str(g)+"?")
    inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if inp == "h":
        high = g
    elif inp == 'l':
        low = g
    elif inp == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")
        continue

print("Game over. Your secret number was:", str(g))