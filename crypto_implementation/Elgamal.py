"""
Author: Missy Shi

Description: Implementation of The Elgamal Public Key Cryptosystem

Date: 11/11/2020
"""

# ------------------------------------- Function Declaration ------------------------------------- #
# prime_check(a: int) -> bool
# fast_powering(n: int, pow: int, modulus: int) -> int
# elgamalEncrypt(m: int, q: int, g: int, bigA: int, k: int) -> list
# elgamalDecrypt(c1: int, c2: int, key: int, q: int) -> int
# elgamal(q: int, g: int, a: int, k: int, m: int) -> list
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


def elgamalEncrypt(m: int, q: int, g: int, bigA: int, k: int) -> list:
    """
    random element k
    Use public key A to compute
        c1 ≡ g^k (mod q)
        c2 ≡ m * (A^k (mod q))
    return ciphertext (c1, c2)
    """
    c1 = fast_powering(g, k, q)
    s = fast_powering(bigA, k, q)
    c2 = (s * m)

    print([c1, c2])
    return [c1, c2]


def elgamalDecrypt(c1: int, c2: int, key: int, q: int) -> int:
    """
    Compute dec_msg = (c1^a)^(−1) · c2 (mod q)
    dec_msg = plaintext m
    return plaintext dec_msg
    """
    h = fast_powering(c1, key, q)
    dec_msg = c2 // h
    return dec_msg


def elgamal(q: int, g: int, a: int, k: int, m: int) -> list:
    """
    return ["0"] if q is not prime
    return [q, g, "0"] if a is not valid
    else return a list:
    [q, g, a, publicKeyA, k, message, encryptedMsg, decryptedMsg]

    example:
    ['23333', '233', '776', '19729', '456', '345', '(16065, 19636)', '345']
    """
    result = []
    # Input prime q, Check if inputs are prime #
    # if not prime, return False, and ask to input again #
    # q = int(input("Input a large prime q: "))
    check_p = prime_check(q)
    if check_p == False:
        result.append("0")
        return result
    else:
        result.append(str(q))
    # print("1")
    # Input an element g: c1 = g^k (mod q) #
    # g = int(input("Input an element g modulo q of large (prime) order: "))
    result.append(str(g))
    # print("2")
    # Input a secret number a: 1 ≤ a ≤ q-1, A = g^a (mod q) #
    # a = int(input("Input a secret number a to act as your private key: "))
    # if a is not valid:
    if a < 1 or a > q-1 or math.gcd(a, q) != 1:
        result.append("0")
        return result
    else:
        result.append(str(a))
    # print("3")

    # Public key A = g^a (mod q), publish it #
    bigA = fast_powering(g, a, q)
    result.append(str(bigA))
    # print("4")

    # Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
    # The number k is called a random element;
    # it exists for the sole purpose of encrypting a single message.
    # k = random.randint(10, 100)
    # k = int(input("Enter a int for your random element k: "))
    if math.gcd(k, q) != 1:
        result.append("0")
        return result
    else:
        result.append(str(k))
    # print("5")

    # message the user wants to encrypt #
    # m = int(input("What would you like to encrypt or decrypt?: "))
    # print(f"Your message is: {m}")
    result.append(str(m))
    # print("6")

    # encrypt the message #
    c1, c2 = elgamalEncrypt(m, q, g, bigA, k)
    result.append(str([c1, c2 % q]))
    # print("7")

    # decrypt the encrypted message #
    dec_msg = elgamalDecrypt(c1, c2, a, q)
    result.append(str(dec_msg))
    # print("8")
    return result

#
# def main():
#     print(elgamal(5293439, 3202, 5039839, 76, 8540))
#
#
# if __name__ == '__main__':
#     main()