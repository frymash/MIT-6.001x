import string
from icecream import ic

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                    another letter (string). 
        '''
        # Define shift_dict
        self.shift_dict = {}
        # Create a tuple containing the alphabetical sets to be shifted
        sets_to_shift = (string.ascii_lowercase, string.ascii_uppercase)
        # for each set in the sets_to_shift:
        for alpha_set in sets_to_shift:
            # for each letter in the set:
            for letter in alpha_set:
                # try: shift each element down by "shift" letters
                try:
                    shifted_letter = alpha_set[alpha_set.index(letter) + shift]
                # except ValueError for non-alphanumeric chars
                except ValueError:
                    pass
                # except IndexError: letters closer to the end of the set can't be shifted beyond the range of the set
                except IndexError:
                    # find how many spots the letter can be shifted before it goes out of range 
                    # calculate the offset -> letter's index + shift - length of alphabet
                    offset = alpha_set.index(letter) + shift - len(alpha_set)
                    # ic(letter,offset,len(alpha_set),alpha_set.index(letter)+1)
                    # implement the offset on the front of the set
                    shifted_letter = alpha_set[offset]
                # add the shifted element to shift_dict
                self.shift_dict[letter] = shifted_letter
        # return shift_dict
        return self.shift_dict

message = Message("test")
ic(message.build_shift_dict(3))