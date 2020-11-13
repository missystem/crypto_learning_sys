"""
Author: Missy Shi
Information: Implementation of RSA Key Exchange
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


def egcd(e, r):
    """ gcd(e,(p-1)(q-1)) = 1 """
    while r != 0:
        e, r = r, e % r
    return e


def eugcd(e, r):
    """ Euclid's Algorithm """
    for i in range(1, r):
        while e != 0:
            a, b = r//e, r % e
            if b != 0:
                print("%d = %d*(%d) + %d" % (r, a, e, b))
            r = e
            e = b


def eea(a, b):
    """ Extended Euclidean Algorithm """
    if a % b == 0:
        return (b, 0, 1)
    else:
        gcd, s, t = eea(b, a % b)
        s = s-((a//b) * t)
        # print("%d = %d*(%d) + (%d)*(%d)" % (gcd, a, t, s, b))
        return (gcd, t, s)


def mult_inv(e, r):
    """ Multiplicative InverseMultiplicative Inverse """
    gcd, s, _ = eea(e, r)
    if gcd != 1:
        return None
    else:
        if s < 0:
            print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d." %
                  (s, s, s % r))
        elif s > 0:
            print("s=%d." % (s))
        return s % r


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


def rsa_encrypt(public: tuple, m: int) -> int:
    """"""
    e, N = public
    ciphertext = (m ** e) % N
    # return the array of bytes
    return ciphertext


def rsa_decrypt(private, c):
    d, n = private
    # print(f"c^d = {c**d}")
    plaintext = (c ** d) % n
    return plaintext


def rsa():
    result = []
    # Input prime numbers q & Check if inputs are prime
    # if not prime, return False, and ask to input again
    p = int(input("Enter a prime number for p: "))
    check_p = prime_check(p)
    if check_p == False:
        result.append("p is not prime")
        return result
    else:
        numberP = "your prime p is: " + str(p) + ". keep it secret"
        result.append(numberP)
    print(numberP)

    # Input prime numbers q & Check if inputs are prime
    q = int(input("Enter a prime number for q: "))
    check_q = prime_check(q)
    if check_q == False:
        result.append("q is not prime")
        return result
    else:
        numberQ = "your prime q is: " + str(q) + ". keep it secret"
        result.append(numberQ)
    print(numberQ)

    #  Calculation of RSA modulus N
    n = p * q
    numberN = "your N = p * q = " + str(n)
    result.append(numberN)
    print(numberN)

    # Calculation of Eulers toitent 'r'
    r = (p-1)*(q-1)
    numberR = "your r = (p-1)(q-1) = " + str(r)
    result.append(numberR)
    print(numberR)

    # 'e' Value Calculation #
    e = int(input("Enter an exponent e between 1 and 1000: "))
    check_e = egcd(e, r)
    if check_e != 1:
        result.append("e is not valid")
        return result
    else:
        numberE = "your exponent e = " + str(e)
        result.append(numberE)
    print(numberE)

    # Public key: publish N = pq and e
    public = (e, n)
    publicKey = "Public Key is: " + str(public) + ". Publish your N and e"
    result.append(publicKey)

    # input message #
    message = int(input("What would you like to encrypt or decrypt?: "))
    print(f"Your message is: {message}")

    enc_msg = rsa_encrypt(public, message)
    ciphertext = "Your encrypted message is: " + str(enc_msg)
    result.append(ciphertext)
    print(ciphertext)

    # d, Private and Public Keys
    # calculation of 'd', private key, and public key.
    # eugcd(e, r)

    d = mul_inverse(e, r)
    numberD = "your d = " + str(d)
    result.append(numberD)
    print(numberD)

    # Private key, 
    private = (d, n)
    privateKey = "Private Key is: " + str(private) + ". Do not give this to anyone"
    result.append(privateKey)
    print(privateKey)

    dec_msg = rsa_decrypt(private, enc_msg)
    plaintext = "Your decrypted message is: " + str(dec_msg)
    result.append(plaintext)
    print(plaintext)

    return result


def main():
    print(rsa())
    # rsa()


if __name__ == "__main__":
    main()
