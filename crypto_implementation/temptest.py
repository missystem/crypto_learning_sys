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
import random
import math


def primePQ(num_prime: int, num_len: int) -> (int, int):
    """generate two prime numbers
    num_prime: number of prime numbers we want in prime list
    num_len: length of prime numbers
    len(p) != len(q), so set q list by using num_len+1
    """
    p_list = randomNumGenerator(num_prime, num_len)
    q_list = randomNumGenerator(num_prime, num_len + 1)
    p = random.choice(p_list)
    p_list.remove(p)
    q = random.choice(q_list)
    q_list.remove(q)
    return p, q


def eGenerator(r):
    """generate a valid e"""
    e = random.randint(1, 1000)
    while math.gcd(e, r) != 1:
        e = random.randint(1, 1000)
    return e


def rsaTester():
    print(f"{'-' * 42} RSA tester {'-' * 42}")
    num_prime = 20
    p, q = primePQ(num_prime, 5)
    # print(f"random prime p = {p}, q = {q}")

    r = (p - 1) * (q - 1)
    e = eGenerator(r)
    # print(f"number e is {e}")
    message = random.randint(100, 1000)
    # print(f"message is {message}")

    if math.gcd(e, (p - 1) * (q - 1)) != 1:
        print("NOOOOOOOOOOOOOOOOOOOOO")
        return

    rsa_result = rsa(p, q, e, message)
    print("[p, q, N, phi, e, publicKey, message, encryptedMsg, d, privateKey, decryptedMsg]")
    print(rsa_result)
    print()
    # simple example result:
    # ['233', '2333', '543589', '541024', '97', '(97, 543589)', '345', '451737', '373697', '(373697, 543589)', '345']


def dhTester():
    print(f"{'-' * 36} Diffie Hellman tester {'-' * 36}")
    print("[p, g, a, b, A, B, A', B']")
    p, q = primePQ(20, 5)
    g = random.randint(10, p)
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    dh_result = diffie_hellman(p, g, a, b)
    print(dh_result)
    print()
    # simple example result:
    # ['2333', '233', '97', '345', '1613', '357', '93', '93']


def elgamalTester():
    print(f"{'-' * 40} Elgamal tester {'-' * 40}")
    print("[p, g, a, publicKeyA, k, message, encryptedMsg, decryptedMsg]")
    p, q = primePQ(20, 5)
    g = random.randint(10, 1000)
    a = random.randint(1, p-1)
    k = random.randint(10, 100)
    m = random.randint(10, 1000)
    elgamal_result = elgamal(p, g, a, k, m)
    print(elgamal_result)
    print()
    # simple example result:
    # ['23333', '233', '776', '19729', '456', '345', '(16065, 19636)', '345']


def subTester():
    print(f"{'-' * 38} Substitution tester {'-' * 38}")
    print("[message, generatedKey, encryptedMsg, decryptedMsg]")
    message = "Hi! How are you? I am good, thank you."
    sub_result = substitution(message)
    print(sub_result)
    print()


def main():
    for i in range(2):
        rsaTester()
        dhTester()
        elgamalTester()

    # subTester()


if __name__ == '__main__':
    main()