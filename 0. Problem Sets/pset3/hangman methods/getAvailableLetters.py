from icecream import ic
from string import ascii_lowercase

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # Take lowercase alphabet set and remove guessed letters.

    # Convert ascii_lowercase to a list and remove any letters which
    # also appear in lettersGuessed to get the unguessed letters
    unguessedLetters = list(ascii_lowercase)
    try:
        for i in lettersGuessed:
            unguessedLetters.remove(i)
    except ValueError:
        print(f"ValueError:{i} couldn't be removed from unguessedLetters")
        exit()
        
    unguessedLetters = ''.join(unguessedLetters)
    return unguessedLetters

secretWord = "affable"

# Test 1: All letters are unguessed
print("--- TEST 1 ---")
lettersGuessed = []
ic(getAvailableLetters(lettersGuessed))

# Test 2: >1 letter is guessed, and >1 letter is unguessed
print("--- TEST 2 ---")
lettersGuessed = ["f","b","l"]
ic(getAvailableLetters(lettersGuessed))

# Test 3: All letters are guessed
print("--- TEST 3 ---")
lettersGuessed = ["a","f","b","l","e"]
ic(getAvailableLetters(lettersGuessed))
