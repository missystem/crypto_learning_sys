"""
Author: Missy Shi
Information: Implementation of Diffie-Hellman Key Exchange
"""


import math


def diffie_hellman():
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



    return result


def main():
    print(diffie_hellman())


if __name__ == '__main__':
    main()