"""
Author: Missy Shi

Date: 11/23/2020

Description: Prime list generator
    For webpage dice using, user clicks dice, it will get a number from dataset
    This file is using for generate those dataset

"""

from prime_list import *
import random
import math


def main():
    num_prime = 20
    prime_list = randomNumGenerator(num_prime, 5)
    print(prime_list)
    # 5-prime lists
    # p_list = [179633, 122201, 130633, 118163, 192889]
    # q_list = [1778993, 1040183, 1215349, 1539389, 1022291]
    # 10-prime list
    # p_list = [161033, 196687, 106703, 183797, 191089, 183041, 134507, 163063, 131969, 111581]
    # q_list = [1192837, 1575137, 1263109, 1951819, 1282529, 1740731, 1465561, 1688909, 1590397, 1745927]
    # 20-prime list
    p_list = [100357, 166429, 116269, 171169, 189529, 182981, 173059, 190529, 189583, 106123, 160483, 105509, 160081, 149161, 144737, 161033, 140159, 176779, 198929, 121487]
    q_list = [1979581, 1096541, 1187353, 1752889, 1484183, 1533127, 1380083, 1029157, 1633553, 1761187, 1008421, 1639367, 1326167, 1674847, 1624507, 1954369, 1163993, 1375637, 1190573, 1076077]

    # This list of e can work with any combination of p & q above
    e_list = [97, 107, 127, 137, 157, 277, 283, 367, 373, 31, 179]
    print(f"length of e list is: {len(e_list)}")
    e_set = set()
    # check to make sure, all numbers can work together (universal lists)
    for e in e_list:
        for p in p_list:
            for q in q_list:
                r = (p - 1) * (q - 1)
                if math.gcd(e, r) == 1:
                    e_set.add(e)
                else:
                    print("this e is not valid!")
                    continue
    print(p_list)
    print(q_list)
    print(len(e_set))
    print(e_set)
    # p = random.choice(prime_list)
    # prime_list.remove(p)
    # q = random.choice(prime_list)
    # prime_list.remove(q)
    # r = (p-1)*(q-1)
    # e = eGenerator(r)
    # e_list = []


if __name__ == '__main__':
    main()