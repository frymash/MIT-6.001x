# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	
# (end of helper code)

def getWordScore(word, n):
    word_score = 0
    for letter in word:
        word_score += SCRABBLE_LETTER_VALUES[letter]
    word_score *= len(word)
    if len(word) == n:
        word_score += 50
    return word_score

# The following function was provided with the course material:
def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")
    print()


# The following function was provided with the course material:
def dealHand(n):
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand


def updateHand(hand, word):

    updated_hand = hand.copy()
    for letter in word:
        updated_hand[letter] -= 1
    return updated_hand


def isValidWord(word, hand, wordList):

    hand_copy = hand.copy()
    if word in wordList:
        try:
            for letter in word:
                if hand_copy[letter] > 0:
                    hand_copy[letter] -= 1
                else:
                    return False
        except:
            return False
        else:
            return True
    return False


def calculateHandlen(hand):
    handLen = sum(hand.values())
    return handLen


def playHand(hand, wordList, n):
    total_score = 0
    while sum(hand.values()) > 0:
        print("Current hand:", end=" ")
        displayHand(hand)
        word = input("Enter word, or a \".\" to indicate that you are finished: ")

        if word == ".":
            break
            
        else:
            if isValidWord(word, hand, wordList) is False:
                print("Invalid word. Please try another word.\n")
            else:
                total_score += getWordScore(word,n)
                print("\"" + word + "\"", "earned", getWordScore(word,n), "points. Total score:", str(total_score), "\n")
                hand = updateHand(hand, word)

    if sum(hand.values()) <= 0:
        print("Run out of letters.", end=" ")
    else:
        print("Goodbye!", end=" ")
    print("Total score:", str(total_score) + ".\n")


def playGame(wordList):
    while True:
        user_input = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")

        if user_input == "n":
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)

        elif user_input == "r":
            try:
                playHand(hand, wordList, HAND_SIZE)
            except:
                print("You have not played a hand yet. Please play a new hand first!")

        elif user_input == "e":
            break

        else:
            print("Invalid command.\n")

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
