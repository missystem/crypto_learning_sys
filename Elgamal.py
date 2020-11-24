"""
Author: Missy Shi
Description: Implementation of The Elgamal Public Key Cryptosystem
Date: 11/11/2020
"""


# ------------------------------------- Function Declaration ------------------------------------- #
# prime_check(a: int) -> bool
# gcdEx(a: int, b: int) -> (int, int, int)
# mul_inverse(e: int, r: int) -> int
# Elgamal_encrypt(m: int, p: int, g: int, bigA: int, k: int)->(int, int)
# Elgamal_decrypt(enc_msg: int, p: int, a:int) -> int
# elgamal()->list
# ------------------------------------------------------------------------------------------------ #


import math


def prime_check(a: int) -> bool:
    """check a number is prime or not
    if it is a prime return True
    else return False"""
    if a == 2:
        return True
    elif (a < 2) or ((a % 2) == 0):
        return False
    elif a > 2:
        for i in range(2, a):
            if not (a % i):
                return False
    return True


def fast_powering(n: int, pow: int, modulus: int) -> int:
    """ Implementation of fast powering algorithm
    :param n: base integer
    :param pow: exponent
    :param modulus: integer modulus
    :return: res = n**pow (mod modulus)
    """
    res = 1
    n = n % modulus
    while pow > 0:
        if int(pow) & 1:
            res = (res * n) % modulus
        pow = int(pow) >> 1
        n = (n * n) % modulus
    return res


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


def Elgamal_encrypt(m: int, p: int, g: int, bigA: int, k: int)->[str, str]:
    """
    random element k
    Use public key A to compute
        c1 ≡ g^k (mod p)
        c2 ≡ mA^k (mod p)
    return ciphertext (c1, c2)
    """
    c1 = fast_powering(g, k, p)
    c2 = (m * (bigA ** k)) % p
    return [str(c1), str(c2)]


def Elgamal_decrypt(enc_msg: [str,str], p: int, a:int) -> int:
    """
    Compute dec_msg = (c1^a)^(−1) · c2 (mod p)
    dec_msg = plaintext m
    return plaintext dec_msg
    """
    c1 = int(enc_msg[0])
    c2 = int(enc_msg[1])
    x = mul_inverse(c1 ** a, p)      # x = (c1 ^ a) ^ (-1) (mod p)
    # print(f"multiplicative inverse of c1^a mod p: {x}")
    dec_msg = (x * c2) % p
    return dec_msg


def elgamal(p, g, a, k, m) -> list:
    """
    return ["0"] if p is not prime
    return [p, g, "0"] if a is not valid
    else return a list:
    [p, g, a, publicKeyA, k, message, encryptedMsg, decryptedMsg]
    example:
    ['23333', '233', '776', '19729', '456', '345', '(16065, 19636)', '345']
    """
    result = []
    p = int(p)
    g = int(g)
    a = int(a)
    k = int(k)
    m = int(m)
    # Input prime numbers p, Check if inputs are prime #
    # if not prime, return False, and ask to input again #
    # p = int(input("Input a large prime p: "))
    check_p = prime_check(p)
    if check_p == False:
        result.append("0")
        return result
    else:
        result.append(str(p))

    # Input an element g: c1 = g^k (mod p) #
    # g = int(input("Input an element g modulo p of large (prime) order: "))
    result.append(str(g))

    # Input a secret number a: 1 ≤ a ≤ p-1, A = g^a (mod p) #
    # a = int(input("Input a secret number a to act as your private key: "))
    # if a is not valid:
    if a < 1 or a > p-1 or math.gcd(a, p) != 1:
        result.append("0")
        return result
    else:
        result.append(str(a))

    # Public key A = g^a (mod p), publish it #
    bigA = fast_powering(g, a, p)
    result.append(str(bigA))

    # Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
    # The number k is called a random element;
    # it exists for the sole purpose of encrypting a single message.
    # k = random.randint(10, 100)
    # k = int(input("Enter a int for your random element k: "))
    if math.gcd(k, p) != 1:
        result.append("0")
        return result
    else:
        result.append(str(k))

    # message the user wants to encrypt #
    # m = int(input("What would you like to encrypt or decrypt?: "))
    # print(f"Your message is: {m}")
    result.append(str(m))

    # encrypt the message #
    enc_msg = Elgamal_encrypt(m, p, g, bigA, k)
    result.append(enc_msg)

    # decrypt the encrypted message #
    print(enc_msg)
    dec_msg = Elgamal_decrypt(enc_msg, p, a)
    result.append(str(dec_msg))

    return result


def main():
    # print(elgamal('2503261', '1796', '807521', '189', '2682'))
    print(elgamal('5293439', '3202', '5039839', '76', '8540'))


if __name__ == '__main__':
    main()