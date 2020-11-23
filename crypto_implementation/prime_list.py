"""
Author: Missy Shi

Description: Generate a list of prime numbers

Date: 11/16/2020
"""


import math
import random


def prime_num(n: int) -> list:
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def primesInRange(n):
    """return a list of prime numbers smaller than n"""
    fact = 1
    primes = []
    for k in range(2, n):
        fact = fact * (k - 1)
        if (fact + 1) % k == 0:
            primes.append(k)
    return primes


def fast_powering(n, pow, modulus):
    res = 1
    n = n % modulus
    while pow > 0:
        if int(pow) & 1:
            res = (res * n) % modulus
        pow = int(pow) >> 1
        n = (n * n) % modulus
    return res


def miller_rabin_test(n: int, a: int) -> bool:
    """ Miller-Rabin Primality Test
    :param n: positive integer to test
    :param a: possible witness (integer < n)
    :return: True if a witness proves that n is composite, False otherwise
    """

    witness = a
    # if n % 2 == 0 or gcd(n, a) != 1 or gcd(n, 2310) != 1:
    if n % 2 == 0 or math.gcd(n, a) != 1 or math.gcd(n, 2310) != 1:
        return True

    k = 0
    q = n - 1
    while q % 2 == 0:
        q = q // 2
        k += 1
    a = fast_powering(a, q, n)
    if (a % n == 1) or (a % n == (n - 1)):
        return False

    for i in range(0, k - 1):
        a = (a ** 2) % n
        if a % n == (n - 1):
            return False
    return True


def mrt_random_a(n: int, num_wit: int) -> int:
    """ miller-rabin test with num_wit random a
    :param n: number for testing
    :param num_wit: check n is prime or not for num_wit times
    return 1 if the number is prime, else return 0
    """
    akspt = int(2 * (math.log(n)) ** 6)
    wit = num_wit
    while num_wit != 0:
        a = random.randint(1, akspt)  # choose random integer as witness
        if miller_rabin_test(n, a) is True:
            # print(f"{n} is not a prime")
            return 0
        num_wit -= 1
    # print(f"Tests failed:\n   {n} is a (probable) prime after test with {wit} different witness.")
    return 1


def randomNumGenerator(num_prime: int, num_len: int) -> list:
    """ Generate a list of prime numbers
    num_prime: number of prime numbers you want in the list
    return a set of prime numbers, use set() to avoid duplicate numbers
    """
    # prime_set = set()
    prime_list = []
    # for i in range(1000):
    while len(prime_list) < num_prime:
        p = random.randint((10 ** num_len), 2 * (10 ** num_len))
        num_wit = 100
        # print(f"Use Miller-Rabin test to check for [{p}] {num_wit} times:")

        if mrt_random_a(p, num_wit) == 1:
            prime_list.append(p)
        else:
            continue
    return prime_list


# def main():
#     num_prime = 20
#     prime_set = randomNumGenerator(num_prime)
#     print()
#     print(f"Length of prime set is: {len(prime_set)}")
#     print()
#     print(f"Prime number set: {prime_set}")
# #
# #     # 740625701, 738983941, 926294489, 131266259, 585402679, 619777843, 15090311101, 10842913889, 13317724991, 19979658533, 18676248001
# #     # 10000000019 | 10000000033 | 10000000061 | 10000000069 | 10000000097 | 10000000103 | 10000000121 | 10000000141 | 10000000147 | 10000000207 | 10000000259 | 10000000277 | 10000000279 | 10000000319 | 10000000343 | 10000000391 | 10000000403 | 10000000469 | 10000000501 | 10000000537 | 10000000583 | 10000000589 | 10000000597 | 10000000601 | 10000000631 | 10000000643 | 10000000649 | 10000000667 | 10000000679 | 10000000711 | 10000000723 | 10000000741 | 10000000753 | 10000000793 | 10000000799 | 10000000807 | 10000000877 | 10000000883 | 10000000889 | 10000000949 | 10000000963 | 10000000991 | 10000000993 | 10000000999 | 10000001041 | 10000001047 | 10000001051 | 10000001057 | 10000001087 | 10000001101 | 10000001113 | 10000001117 | 10000001153 | 10000001159 | 10000001251 | 10000001371 | 10000001377 | 10000001383 | 10000001411 | 10000001419 | 10000001437 | 10000001441 | 10000001467 | 10000001471 | 10000001519 | 10000001533 | 10000001551 | 10000001593 | 10000001623 | 10000001651 | 10000001659 | 10000001677 | 10000001689 | 10000001707 | 10000001723 | 10000001743 | 10000001747 | 10000001797 | 10000001813 | 10000001861 |
# #
# #
# if __name__ == '__main__':
#     main()