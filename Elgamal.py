"""
Author: Missy Shi
Information: Implementation of The Elgamal Public Key Cryptosystem
"""

import math
import random


def prime_check(a):
    if a == 2:
        return True
    elif (a < 2) or ((a % 2) == 0):
        return False
    elif a > 2:
        for i in range(2, a):
            if not (a % i):
                return False
    return True


def gcdEx(a: int, b: int) -> (int, int, int):
    """ Extended Euclidean Algorithm """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = gcdEx(b % a, a)
        return (g, x - (b // a) * y, y)


def mul_inverse(e: int, r: int) -> int:
    """
    Find the multiplicative inverse of e (d) mod r
    r = (p-1)(q-1)
    ed = 1 (mod r)
    :param e: integer
    :param r: modulus
    :return: integer e^(-1) (mod r)
    """
    g, x, y = gcdEx(e, r)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % r


def Elgamal_encrypt(m, p, g, bigA):
    """"""
    k = random.randint(10, 100)   # Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
    c1 = (g ** k) % p
    c2 = (m * (bigA ** k)) % p
    return (c1, c2)


def Elgamal_decrypt(enc_msg, p, a):
    c1, c2 = enc_msg
    x = mul_inverse(c1 ** a, p)      # x = (c1 ^ a) ^ (-1) (mod p)
    dec_msg = (x * c2) % p
    return dec_msg


def elgamal():
    result = []
    p = int(input("Input a large prime p: "))
    check_p = prime_check(p)
    if check_p == False:
        result.append("p is not prime")
        return result
    else:
        numberP = "your prime p is: " + str(p)
        result.append(numberP)
    print(numberP)

    g = int(input("Input an element g modulo p of large (prime) order: "))
    numberG = "Your element g is: " + str(g)
    result.append(numberG)
    print(numberG)

    a = int(input("Input a secret number a to act as your private key: "))
    if a < 1 or a > p-1:
        result.append("a is not valid, a should be 1 ≤ a ≤ p-1")
        return result
    else:
        number_a = "Your number a is: " + str(a)
        result.append(number_a)
    print(number_a)

    bigA = (g ** a) % p
    numberA = "Your public key A = g ^ a (mod p) is: " + str(bigA) + ". Publish it."
    result.append(numberA)
    print(numberA)

    m = int(input("What would you like to encrypt or decrypt?: "))
    print(f"Your message is: {m}")

    enc_msg = Elgamal_encrypt(m, p, g, bigA)
    ciphertext = "Your encrypted message is: " + str(enc_msg)
    result.append(ciphertext)
    print(ciphertext)

    dec_msg = Elgamal_decrypt(enc_msg, p, a)
    plaintext = "Your decrypted message is: " + str(dec_msg)
    result.append(plaintext)
    print(plaintext)

    return result


def main():
    print(elgamal())


if __name__ == '__main__':
    main()
