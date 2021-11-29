# Hangman game (pset3)
# Edited by ozervesh on Tue 23 Nov 2021, 2:16pm
# Took approximately 3h 30min to write and completely debug

# Autograder doesn't like fstrings and having string.ascii_lowercase as ascii_lowercase.

import random
import string
from icecream import ic

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # secretWordLetters = ic(list(secretWord))
    secretWordLetters = list(secretWord)
    if set(secretWordLetters).issubset(set(lettersGuessed)):
        return True
    return False

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
    # ic(lettersGuessedSoFar)
    lettersGuessedSoFar = ''.join(lettersGuessedSoFar)
    return lettersGuessedSoFar

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    # Take lowercase alphabet set and remove guessed letters.

    # Convert ascii_lowercase to a list and remove any letters which
    # also appear in lettersGuessed to get the unguessed letters
    unguessedLetters = list(string.ascii_lowercase)

    for i in lettersGuessed:
        unguessedLetters.remove(i)
        
    unguessedLetters = ''.join(unguessedLetters)
    return unguessedLetters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    print("-------------")
    lettersGuessed = []
    guesses_left = 8

    while True:
      print("You have", guesses_left, "guesses left.")
      # At the start of the game, let the user know how many letters the 
      # secretWord contains.
      print("Available letters:", getAvailableLetters(lettersGuessed))

      # Ask the user to supply one guess (i.e. letter) per round.
      while True:
        guess = input("Please guess a letter: ")

        # to account for blank guesses
        if guess == "":
          print("You haven't entered a letter, please try again.\n")
          continue

        # to account for punctuation marks and non-Latin letters
        elif len(guess) != 1 or guess not in string.ascii_lowercase: 
          print("Your guess was", guess, ", which isn't a letter in the alphabet. Please try again.")
          continue

        break

      guess = guess.lower()

      # The user should receive feedback immediately after each guess 
      # about whether their guess appears in the computers word.

      # After each round, you should also display to the user the partially
      # guessed word so far, as well as letters that the user has not yet guessed.

      # Personal note:
      # I was thinking of modularising lines 151-157 and 161-167 and defining
      # a function which can replace these snippets. However, it doesn't seem
      # 100% intuitive so I'll pass on that for now.

      if guess in secretWord:
        if guess not in lettersGuessed:
          lettersGuessed.append(guess)
          print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        else: # guess in lettersGuessed
          print("Oops! You've already guessed that letter:",\
                  getGuessedWord(secretWord, lettersGuessed))

      else: # elif guess not in secretWord
        if guess not in lettersGuessed:
          lettersGuessed.append(guess)
          print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
          guesses_left -= 1
        else: # guess in lettersGuessed
          print("Oops! You've already guessed that letter:",\
                  getGuessedWord(secretWord, lettersGuessed))

      print("-------------")

      # If all the letters in the word are guessed, break the loop and end the game.
      # Else (elif there are words remaining), -1 from guesses_left. 
        # If guesses_left is 0, end the game.
        # Otherwise, start a new guess

      # ic(lettersGuessed)
      # ic(isWordGuessed(secretWord, lettersGuessed))
      if isWordGuessed(secretWord, lettersGuessed) is True:
        print("Congratulations, you won!")
        break
      else:
        if guesses_left == 0:
          print("Sorry, you ran out of guesses. The word was", secretWord)
          break


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# For testing:
# secretWord = "affable"
# hangman(secretWord)

# To run the full game:
# secretWord = ic(chooseWord(wordlist).lower())
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
