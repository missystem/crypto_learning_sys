"""
Author: Missy Shi

Description: temporary file for testing algorithm implementations

Date: 11/13/2020
"""


from RSA import *
from DH import *
from Elgamal import *
from substitution import *
from prime_list import *


def main():
    # generate 20 prime numbers
    # num_prime = 2
    # prime_list = randomNumGenerator(num_prime)
    # p = random.choice(prime_list)
    # prime_list.remove(p)
    # q = random.choice(prime_list)
    # prime_list.remove(q)
    # print(f"random item from list is: {p}, and {q}")
    #
    # # rsa_result = rsa(233, 2333, 97, 345)
    # e = random.randint(1, 1000)
    # print(f"number e is {e}")
    # message = random.randint(100, 1000)
    # print(f"message is {message}")
    print("-" * 100)
    p = 23
    q = 31
    e = 61
    message = 100
    rsa_result = rsa(p, q, e, message)
    print("[p, q, N, phi, e, publicKey, message, encryptedMsg, d, privateKey, decryptedMsg]")
    print(rsa_result)
    print("-" * 100)
    print()
    # ['233', '2333', '543589', '541024', '97', '(97, 543589)', '345', '451737', '373697', '(373697, 543589)', '345']

    print("=" * 100)
    print("[p, g, a, b, A, B, A', B']")
    dh_result = diffie_hellman(2333, 233, 97, 345)
    print(dh_result)
    print("=" * 100)
    print()
    # ['2333', '233', '97', '345', '1613', '357', '93', '93']

    print("[p, g, a, publicKeyA, k, message, encryptedMsg, decryptedMsg]")
    elgamal_result = elgamal(23333, 233, 776, 456, 345)
    print(elgamal_result)
    # ['23333', '233', '776', '19729', '456', '345', '(16065, 19636)', '345']
    print()


    print("-------------------------")
    print("[message, generatedKey, encryptedMsg, decryptedMsg]")
    message = "Hi! How are you? I am good, thank you."
    sub_result = substitution(message)
    print(sub_result)
    print()


if __name__ == '__main__':
    main()