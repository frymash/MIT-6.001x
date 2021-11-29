# Edited by ozervesh on Mon 29 Nov, 4:48pm
# Took approximately 5 hours to fully edit and debug

from os import get_terminal_size
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

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
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
    
    def get_shift_dict(self):
        return self.shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # build shift dictionary based on the shift parameter
        self.build_shift_dict(shift)

        # get message text and convert it from str -> list
        message = list(self.get_message_text())
        # for each letter in the message, 
        shifted_message = []
        for letter in message:
            # try: shift the letter into its 'shifted letter' in accordance to self.shift_dict
            try:
                shifted_message.append(self.get_shift_dict()[letter])
            # except KeyError: non-alphanumeric characters
            except KeyError:
                shifted_message.append(letter)
        # join the list into a str
        shifted_message = "".join(shifted_message)
        # return the str with the shifted letters
        return shifted_message

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        # Use parent class __init__ method to init self.message_text and self.valid_words
        Message.__init__(self,text)
        # init self.shift from parameter
        self.shift = int(shift)
        # init self.encrypting_dict by running Message.build_shift_dict(self,shift)
        self.encrypting_dict = Message.build_shift_dict(self,shift)
        # init self.message_text_encrypted by running Message.apply_shift(self,shift)
        self.message_text_encrypted = Message.apply_shift(self,shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        encrypted_dict_copy = self.encrypting_dict.copy()
        return encrypted_dict_copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        # Redefine self.shift from new shift
        self.shift = int(shift)
        # Redefine self.encrypting_dict by re-running Message.build_shift_dict(self,shift)
        self.encrypting_dict = Message.build_shift_dict(self,shift)
        # Redefine self.message_text_encrypted by re-running Message.apply_shift(self,shift)
        self.message_text_encrypted = Message.apply_shift(self,shift)

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # Reuse Message's init function to construct self.message_text and self.valid_words.
        Message.__init__(self,text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # Define best_shift and best_message
        best_shift = None
        best_message = ""
        # Define the highest. amount of real words found so far
        highest_real_words = 0
        # For every possible shift between 0-25 (excluding 26 since that would mean nothing is shifted):
        for s in range(26):
            # Apply shift to message and convert message to list
            message = self.get_message_text()
            decrypted_message = self.apply_shift(s)
            decrypted_message_list = decrypted_message.split()
            # Define no. of real words counted so far
            real_words = 0
            # For each word in the message:
            for word in decrypted_message_list:
                # Check if the word is valid. If the word is valid, add it to real_words
               if is_word(self.get_valid_words(), word):
                   real_words += 1
            # if this shift has produced the most real_words so far, designate it as best_shift
            if real_words > highest_real_words:
                highest_real_words = real_words
                best_shift = s
                best_message = decrypted_message
        
        # return as per docstr
        return best_shift, best_message

def decrypt_story():
    '''
    inputs: None

    returns: the decrypted story.txt string
    '''
    story = CiphertextMessage(get_story_string())
    return story.decrypt_message()

ic(decrypt_story())
        
'''
# Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())

# Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())
'''
