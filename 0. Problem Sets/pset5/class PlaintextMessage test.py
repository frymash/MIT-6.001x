from ps6 import Message
from icecream import ic

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
        # init self.message_text_encrypted by running Message.apply_shift(self,text)
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
        # init self.shift from parameter
        self.shift = int(shift)
        # init self.encrypting_dict by running Message.build_shift_dict(self,shift)
        self.encrypting_dict = Message.build_shift_dict(self,shift)
        # init self.message_text_encrypted by running Message.apply_shift(self,text)
        self.message_text_encrypted = Message.apply_shift(self,shift)

test1 = ic(PlaintextMessage("1.hello!!", 7))
ic(test1.get_shift())

test2 = ic(PlaintextMessage("1.hello!!", 9))
ic(test2.get_encrypting_dict())

test3 = ic(PlaintextMessage("1.hello!!", 2))
ic(test3.get_message_text_encrypted())
