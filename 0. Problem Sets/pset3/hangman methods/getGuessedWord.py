from icecream import ic

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    lettersGuessedSoFar = []
    for i in secretWord:
        if i in lettersGuessed:
            lettersGuessedSoFar.append(i)
        else:
            lettersGuessedSoFar.append("_")
    ic(lettersGuessedSoFar)
    lettersGuessedSoFar = ''.join(lettersGuessedSoFar)
    return lettersGuessedSoFar


secretWord = 'affable'

# Test 1: no letters in secretWord guessed; 0 letters returned
print("--- TEST 1 ---")
lettersGuessed = []
ic(lettersGuessed)
ic(getGuessedWord(secretWord, lettersGuessed))
print("\n")

# Test 2: some letters in secretWord guessed; 50% of letters returned
print("--- TEST 2 ---")
lettersGuessed = ['f','b','l']
ic(lettersGuessed)
ic(getGuessedWord(secretWord, lettersGuessed))
print("\n")

# Test 3: all letters in secretWord guessed; all letters returned
print("--- TEST 3 ---")
lettersGuessed = ['a','f','b','l','e']
ic(lettersGuessed)
ic(getGuessedWord(secretWord, lettersGuessed))
print("\n")
