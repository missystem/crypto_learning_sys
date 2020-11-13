"""
Author: Missy Shi
Information: Implementation of Diffie-Hellman Key Exchange
"""


import math


def prime_check(a: int) -> bool:
    """ check for a integer is prime or not """
    if a == 2:
        return True
    elif (a < 2) or ((a % 2) == 0):
        return False
    elif a > 2:
        for i in range(2, a):
            if not (a % i):
                return False
    return True


def diffie_hellman():
    """
    return ["0"] if p is not prime
    else return a list:
    [p, g, a, b, A, B, A', B', ]
    """
    result = []

    # public number p & g #
    # Input prime p, Check if input is prime #
    # if not prime, return False, and ask to input again #
    p = int(input("Enter a prime number for p: "))
    check_p = prime_check(p)
    if check_p == False:
        result.append("0")
    else:
        result.append(str(p))

    # it is best if they choose g such that its order in Fp* is a large prime.
    g = int(input("Input an element g modulo p of large (prime) order: "))
    result.append(str(g))

    # A picks a secret integer a, do not reveal to anyone
    a = int(input("Enter a secret integer a: "))
    result.append(str(a))

    # B picks a secret integer b, do not reveal to anyone
    b = int(input("Enter a secret integer b: "))
    result.append(str(b))

    # A computes A ≡ g^a (mod p):
    bigA = (g ** a) % p
    result.append(str(bigA))
    # B computes B ≡ g^b (mod p):
    bigB = (g ** b) % p
    result.append(str(bigB))

    # They next exchange these computed values,
    # Alice sends A to Bob and Bob sends B to Alice.
    # Note that Eve gets to see the values of A and B,
    # since they are sent over the insecure communication channel.
    # B and A again use their secret integers to compute
    # A' = B^a (mod p)
    bigA_ = (bigB ** a) % p
    result.append(str(bigA_))
    # B' = A^b (mod p)
    bigB_ = (bigA ** b) % p
    result.append(str(bigB_))

    # The values that they compute,
    # A′ and B′ respectively, are actually the same,
    # since A′ ≡ B^a ≡ (g^b)^a ≡ g^(ab) ≡ (g^a)^b ≡ A^b ≡ B′ (mod p)

    return result


def main():
    print(diffie_hellman())


if __name__ == '__main__':
    main()