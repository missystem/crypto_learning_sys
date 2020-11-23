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
    """return encrypted message"""
    e, N = public
    ciphertext = (m ** e) % N
    # return the array of bytes
    return ciphertext


def rsa_decrypt(private, c):
    """return decrypted message"""
    d, n = private
    # print(f"c^d = {c**d}")
    plaintext = (c ** d) % n
    return plaintext


def rsa(p, q, e, message):
    """
    return: [p, q, N, r, e, publicKey, encryptedMsg, d, privateKey, decryptedMsg]
    """
    result = []
    # Input prime numbers q & Check if inputs are prime #
    # if not prime, return False, and ask to input again #
    p = int(p)
    check_p = prime_check(p)
    if check_p == False:
        result.append("0")
    else:
        result.append(str(p))

    # Input prime numbers q & Check if inputs are prime #
    q = int(q)
    check_q = prime_check(q)
    if check_q == False:
        result.append("0")
    else:
        result.append(str(q))

    # if p or q is not prime, return a small list #
    if result[0] == "0" or result[1] == "0":
        return result

    #  Calculation of RSA modulus N #
    n = p * q
    result.append(str(n))

    # Calculation of Eulers toitent 'r' #
    r = (p-1)*(q-1)
    result.append(str(r))

    # 'e' Value Calculation #
    e = int(e)
    check_e = egcd(e, r)
    if check_e != 1:
        result.append("0")
        return result
    else:
        result.append(str(e))

    # Public key: publish N = pq and e #
    public = (e, n)
    result.append(str(public))

    # input message #
    message = int(message)
    print(f"Your message is: {message}")

    # encrypt message #
    enc_msg = rsa_encrypt(public, message)
    result.append(str(enc_msg))

    d = mul_inverse(e, r)
    result.append(str(d))

    # Private key: d and N = pq (keep d private) #
    private = (d, n)
    result.append(str(private))

    # decrypt message #
    dec_msg = rsa_decrypt(private, enc_msg)
    result.append(str(dec_msg))

    return result


def main():
    print(rsa())


if __name__ == "__main__":
    main()