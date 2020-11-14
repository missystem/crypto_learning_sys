"""
Author: Missy Shi

Description: temporary file for testing algorithm implementations

Date: 11/13/2020
"""


from RSA import *
from DH import *
from Elgamal import *

def main():
    rsa_result = rsa(233, 2333, 97, 345)
    print("[p, q, N, r, e, publicKey, message, encryptedMsg, d, privateKey, decryptedMsg]")
    print(rsa_result)
    print()
    # ['233', '2333', '543589', '541024', '97', '(97, 543589)', '345', '451737', '373697', '(373697, 543589)', '345']

    print("[p, g, a, b, A, B, A', B']")
    dh_result = diffie_hellman(2333, 233, 97, 345)
    print(dh_result)
    print()
    # ['2333', '233', '97', '345', '1613', '357', '93', '93']

    print("[p, g, a, publicKeyA, k, message, encryptedMsg, decryptedMsg]")
    elgamal_result = elgamal(23333, 233, 776, 456, 345)
    print(elgamal_result)
    # ['23333', '233', '776', '19729', '456', '345', '(16065, 19636)', '345']


if __name__ == '__main__':
    main()