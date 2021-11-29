import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    secretWordLetters = list(secretWord)
    if set(secretWordLetters).issubset(set(lettersGuessed)):
        return True
    return False

def getGuessedWord(secretWord, lettersGuessed):
    lettersGuessedSoFar = []
    for i in secretWord:
        if i in lettersGuessed:
            lettersGuessedSoFar.append(i)
        else:
            lettersGuessedSoFar.append("_")
    lettersGuessedSoFar = ''.join(lettersGuessedSoFar)
    return lettersGuessedSoFar

def getAvailableLetters(lettersGuessed):
    unguessedLetters = list(string.ascii_lowercase)
    for i in lettersGuessed:
        unguessedLetters.remove(i)
    unguessedLetters = ''.join(unguessedLetters)
    return unguessedLetters

def hangman(secretWord):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    print("-------------")
    lettersGuessed = []
    guesses_left = 8

    while True:
      print("You have", guesses_left, "guesses left.")
      print("Available letters:", getAvailableLetters(lettersGuessed))

      while True:
        guess = input("Please guess a letter: ")

        if guess == "":
          print("You haven't entered a letter, please try again.\n")
          continue

        elif len(guess) != 1 or guess not in string.ascii_lowercase: 
          print("Your guess was", guess, ", which isn't a letter in the alphabet. Please try again.")
          continue

        break

      guess = guess.lower()

      if guess in secretWord:
        if guess not in lettersGuessed:
          lettersGuessed.append(guess)
          print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        else:
          print("Oops! You've already guessed that letter:",\
                  getGuessedWord(secretWord, lettersGuessed))

      else:
        if guess not in lettersGuessed:
          lettersGuessed.append(guess)
          print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
          guesses_left -= 1
        else:
          print("Oops! You've already guessed that letter:",\
                  getGuessedWord(secretWord, lettersGuessed))

      print("-------------")

      if isWordGuessed(secretWord, lettersGuessed) is True:
        print("Congratulations, you won!")
        break
      else:
        if guesses_left == 0:
          print("Sorry, you ran out of guesses. The word was", secretWord)
          break

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
