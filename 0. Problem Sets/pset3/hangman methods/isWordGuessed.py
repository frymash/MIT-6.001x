from icecream import ic

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWordLetters = ic(list(secretWord))
    if set(secretWordLetters).issubset(set(lettersGuessed)):
        return True
    return False

secretWord = "affable"

# Test 1: True if all the letters of secretWord are in lettersGuessed
print("--- TEST 1 ---")
lettersGuessed = ['a','f','b','l','e']
ic(lettersGuessed)
ic(isWordGuessed(secretWord, lettersGuessed))

print("\n")

# Test 2: False otherwise
print("--- TEST 2 ---")
lettersGuessed = ['a','e']
ic(lettersGuessed)
ic(isWordGuessed(secretWord, lettersGuessed))

print("\n")

# Test 3: True - Correct letters are guessed, but other wrong letters are also guessed
print("--- TEST 3 ---")
lettersGuessed = ['a','b','c','e','f','l','z']
ic(lettersGuessed)
ic(isWordGuessed(secretWord, lettersGuessed))
