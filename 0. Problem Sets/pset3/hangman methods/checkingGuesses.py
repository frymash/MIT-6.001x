from icecream import ic

from getGuessedWord import getGuessedWord

guesses_left = int()

def checkingGuesses(message, secretWord, guess, lettersGuessed):
    """
    This function checks if the letter guessed has been already
    been guessed in a previous attempt. 
    
    If the letter hasn't been guessed before, 
    a. it will be added to the list of letters which have already been guessed and
    b. the no. of guesses left will be decremented by 1.

    inputs:
    1. message
        - str; a message the console will print if the guess hasn't been entered before
    2. secretWord
        - str; the word to be guessed
    3. guess
        - str; the letter the user is using as a guess
    4. lettersGuessed
        - List; a list of all the letters guessed so far

    returns: None

    """
    global guesses_left
    if guess not in lettersGuessed:
            lettersGuessed.append(guess)
            print(message, getGuessedWord(secretWord, lettersGuessed))
            guesses_left -= 1
    else: # guess in lettersGuessed
        print("Oops! You've already guessed that letter:",\
                getGuessedWord(secretWord, lettersGuessed))

