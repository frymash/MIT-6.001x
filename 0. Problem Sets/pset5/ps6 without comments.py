from os import get_terminal_size
import string
from icecream import ic

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    print('Loading word list from file...')
    in_file = open(file_name, 'r')
    line = in_file.readline()
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):

        self.shift_dict = {}
        sets_to_shift = (string.ascii_lowercase, string.ascii_uppercase)
        for alpha_set in sets_to_shift:
            for letter in alpha_set:
                try:
                    shifted_letter = alpha_set[alpha_set.index(letter) + shift]
                except ValueError:
                    pass
                except IndexError:
                    offset = alpha_set.index(letter) + shift - len(alpha_set)
                    shifted_letter = alpha_set[offset]
                self.shift_dict[letter] = shifted_letter
        return self.shift_dict
    
    def get_shift_dict(self):
        return self.shift_dict

    def apply_shift(self, shift):
        self.build_shift_dict(shift)
        message = list(self.get_message_text())
        shifted_message = []
        for letter in message:
            try:
                shifted_message.append(self.get_shift_dict()[letter])
            except KeyError:
                shifted_message.append(letter)
        shifted_message = "".join(shifted_message)
        return shifted_message

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        Message.__init__(self,text)
        self.shift = int(shift)
        self.encrypting_dict = Message.build_shift_dict(self,shift)
        self.message_text_encrypted = Message.apply_shift(self,shift)

    def get_shift(self):
        return self.shift

    def get_encrypting_dict(self):
        encrypted_dict_copy = self.encrypting_dict.copy()
        return encrypted_dict_copy

    def get_message_text_encrypted(self):
        return self.message_text_encrypted

    def change_shift(self, shift):
        self.shift = int(shift)
        self.encrypting_dict = Message.build_shift_dict(self,shift)
        self.message_text_encrypted = Message.apply_shift(self,shift)

class CiphertextMessage(Message):
    def __init__(self, text):
        Message.__init__(self,text)

    def decrypt_message(self):
        best_shift = None
        best_message = ""
        highest_real_words = 0
        for s in range(26):
            message = self.get_message_text()
            decrypted_message = self.apply_shift(s)
            decrypted_message_list = decrypted_message.split()
            real_words = 0
            for word in decrypted_message_list:
               if is_word(self.get_valid_words(), word):
                   real_words += 1
            if real_words > highest_real_words:
                highest_real_words = real_words
                best_shift = s
                best_message = decrypted_message
        return best_shift, best_message

def decrypt_story():

    story = CiphertextMessage(get_story_string())
    return story.decrypt_message()

ic(decrypt_story())
