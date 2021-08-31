from en_de_function import *
from main import *
from collections import Counter
import hashlib
import random
import string
import base64


#functions for required encryption/decryption

def str_to_bin(s):
    res = ''.join(format(ord(i), 'b') for i in s)
    return str(res)

def bin_to_str(b):
    binary_values = b.split()
    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string+=ascii_character
    return ascii_string

def dec_to_bin(n):
    return bin(n).replace("0b", "")

def bin_to_dec(b):
    return int(b,2)

def freq_analysis(s):
    return Counter(s)

def rev_str(s):
    return s[::-1]

def str_to_caesar(message,shift):
    dict1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
             'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
             'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
             'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
             'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

    dict2 = {0: 'Z', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
             6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
             11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
             16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
             21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y'}
    message = message.upper()
    cipher = ''
    for letter in message:
        if (letter != ' '):
            num = (dict1[letter] + shift) % 26
            cipher += dict2[num]
        else:
            cipher += ' '

    return cipher

def caesar_to_str(message, shift):
    dict1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
             'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
             'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
             'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
             'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

    dict2 = {0: 'Z', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
             6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
             11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
             16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
             21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y'}
    message = message.upper()
    decipher = ''
    for letter in message:
        if (letter != ' '):
            num = (dict1[letter] - shift + 26) % 26
            decipher += dict2[num]
        else:
            decipher += ' '

    return decipher

def str_to_base64(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

def base64_to_str(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message

#hashing algorithms function
def str_to_md5(s):
    return (hashlib.md5(s.encode())).hexdigest()

def str_to_saltedmd5(s):
    n=random.randrange(4,8)
    chars=string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation
    salted_str = ''.join(random.choice(chars) for _ in range(n))
    s+=salted_str
    return (hashlib.md5(s.encode())).hexdigest()

def str_to_sha1(s):
    return (hashlib.sha1(s.encode())).hexdigest()

def str_to_sha256(s):
    return (hashlib.sha256(s.encode())).hexdigest()

def str_to_sha512(s):
    return (hashlib.sha512(s.encode())).hexdigest()
