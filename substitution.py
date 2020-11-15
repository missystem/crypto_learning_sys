"""
Author: Missy Shi

Description: Implementation of Substitution Cipher

Date: 11/13/2020

Notes:
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    hexdigits = '0123456789abcdefABCDEF'
    octdigits = '01234567'
    printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    whitespace = ' \t\n\r\x0b\x0c'

Credits:
    https://stackoverflow.com/questions/36188226/substitution-cipher-python
"""

# ------------------------------------- Function Declaration ------------------------------------- #
# prime_check(a: int) -> bool
# fast_powering(n: int, pow: int, modulus: int) -> int
# diffie_hellman(p: int, g: int, a: int, b: int) -> list
# ------------------------------------------------------------------------------------------------ #


import string
import random


def makeKey(alphabet: str) -> str:
    """Generate a random key by shuffle alphabet"""
    alphabet = list(alphabet)
    random.shuffle(alphabet)
    return ''.join(alphabet)


def subEncrypt(message, key, alphabet):
    keyIndices = [alphabet.index(k.lower()) for k in message]
    return ''.join(key[keyIndex] for keyIndex in keyIndices)


def subDecrypt(enc_msg, key, alphabet):
    keyIndices = [key.index(k) for k in enc_msg]
    return ''.join(alphabet[keyIndex] for keyIndex in keyIndices)


def substitution(message):
    """
    Only '.,!? ' are allowed to use in message
    return ['0'] if some invalid symbol exists in message
    example: "I'm good" (' is not valid)
    else return:
    [message, generatedKey, encryptedMsg, decryptedMsg]
    """
    result = []
    alphabet = string.ascii_lowercase + '.,!? '

    for i in message:
        if i.lower() not in alphabet:
            print(i)
            result.append('0')
            return result

    result.append(message)

    key = makeKey(alphabet)
    # print(f"the random generated key is: {key}")
    result.append(key)

    enc_msg = subEncrypt(message, key, alphabet)
    # print(f"Your encrypted message is: {enc_msg}")
    result.append(enc_msg)

    dec_msg = subDecrypt(enc_msg, key, alphabet)
    # print(f"Your decrypted message is: {dec_msg}")
    result.append(dec_msg)

    return result



# def main():
#     message = str(input("Enter the message you want to encrypt: "))
#     print(f"Your message is: {message}")
#     substitution(message)
#
#
# if __name__ == '__main__':
#     main()