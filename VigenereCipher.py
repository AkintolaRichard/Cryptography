#! python3
# Cryptography.py - This program is about cyptography using Vigenere Cipher

class Cryptography:
    """A class to encrypt and decrypt using the Vigenere Cipher."""

    def __init__(self, key):
        """Initializing the class and declaring the variables."""
        self.encrypted_text = ''
        self.decrypted_text = ''
        self.key = key.lower()
        self._dictionary = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, '$': 26}
    
    def encryption(self, plaintext):
        """This method accepts the plain text and returns the encrypted text."""
        self.message = plaintext.lower().replace(' ', '$')
        self.keyIndex = 0
        self._check_encryption_and_evaluate()
        return self.encrypted_text.upper()

    def _check_encryption_and_evaluate(self):
        for i in self.message:
            if self.keyIndex == len(self.key):
                self.keyIndex = 0
                for k, v in self._dictionary.items():
                    if v == ((self._dictionary.get(i) + self._dictionary.get(self.key[self.keyIndex])) % 27):
                        self.encrypted_text += str(k)
                self.keyIndex += 1
            else:
                for k, v in self._dictionary.items():
                    if  v == ((self._dictionary.get(i) + self._dictionary.get(self.key[self.keyIndex])) % 27):
                        self.encrypted_text += str(k)
                self.keyIndex += 1
    
    
    def decryption(self, encryptedtext):
        """This method accepts the encrypted text and returns the decrypted (plain) text."""
        self.encrypted_text = encryptedtext.lower()
        self.keyIndex = 0
        self.decrypted_text = ''
        self._check_decryption_and_evaluate()
        self.decrypted_text = self.decrypted_text.replace('$', ' ')
        return self.decrypted_text.capitalize()
    
    def _check_decryption_and_evaluate(self):
        for i in self.encrypted_text:
            if self.keyIndex == len(self.key):
                self.keyIndex = 0
                for k, v in self._dictionary.items():
                    if v == ((self._dictionary.get(i) - self._dictionary.get(self.key[self.keyIndex])) % 27):
                        self.decrypted_text += str(k)
                self.keyIndex += 1
            else:
                for k, v in self._dictionary.items():
                    if v == ((self._dictionary.get(i) - self._dictionary.get(self.key[self.keyIndex])) % 27):
                        self.decrypted_text += str(k)
                self.keyIndex += 1

# Testing the code.
text = "Take down the man with a red hat by two pm"
key = "hackaton"
crypto = Cryptography(key)
myencrypted_text = crypto.encryption(text)
myDecryption = crypto.decryption(myencrypted_text)

print(f"Text: {text}\nEncypted Text: {myencrypted_text}")
print()
print(f"Encrypted Text: {myencrypted_text}\nDecrypted Text: {myDecryption}")




















































