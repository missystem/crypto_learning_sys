"""
Author: Missy Shi
"""

import math


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


def encrypt(public: tuple, m: int) -> int:
    e, N = public
    ciphertext = (m ** e) % N
    # return the array of bytes
    return ciphertext


def decrypt(private, m):
    d, n = private
    plaintext = (c ** d) % n
    return plaintext


def rsa():
    # Input prime numbers q & Check if inputs are prime
    # if not prime, return False, and ask to input again
    p = int(input("Enter a prime number for p: "))
    check_p = prime_check(p)
    while check_p == False:
        print("p is not prime.")
        p = int(input("Enter a prime number for p: "))
        check_p = prime_check(p)
    # Input prime numbers q & Check if inputs are prime
    q = int(input("Enter a prime number for q: "))
    check_q = prime_check(q)
    while check_q == False:
        print("q is not prime.")
        q = int(input("Enter a prime number for q: "))
        check_q = prime_check(q)

    #  Calculation of RSA modulus N
    n = p * q

    # Calculation of Eulers toitent 'r'
    r = (p-1)*(q-1)

    # 'e' Value Calculation #
    e = int(input("Enter an exponent e between 1 and 1000: "))
    check_e = egcd(e, r)
    while check_e != 1:
        print("e is not valid.")
        p = int(input("Enter an exponent e between 1 and 1000: "))
        check_e = egcd(e, r)

    # d, Private and Public Keys
    # calculation of 'd', private keey, and public key.
    # eugcd(e, r)

    d = mult_inv(e, r)

    # Public key: publish N = pq and e
    public = (e, n)
    # Private key, 
    private = (d, n)
    print(f"Private Key is: {private}. Do not give this to anyone")
    print(f"Public Key is: {public}. Publish N = pq and e")

    # input message #
    message = int(input("What would you like encrypted or decrypted?: "))
    print(f"Your message is: {message}")

    # Choose Encrypt or Decrypt and Print #
    method = input("Select 'enc' for encryption, or 'dec' for decryption: ")
    if method == 'enc':
        enc_msg = encrypt(public, message)
        print("Your encrypted message is:", enc_msg)
    elif method == 'dec':
        print("Your decrypted message is:", decrypt(private, message))
    else:
        print("Wrong method, please input 'enc' for encryption, or 'dec' for decryption: ")
    
    return None


def main():
    rsa()


if __name__ == "__main__":
    main()
