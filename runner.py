from rsa_method import *

def rsa():
    # Input prime numbers p, q & Check if inputs are prime
    p = int(input("Enter a prime number for p: "))
    check_p = prime_check(p)
    while check_p == False:
        print("p is not prime.")
        p = int(input("Enter a prime number for p: "))
        check_p = prime_check(p)
    q = int(input("Enter a prime number for q: "))    
    check_q = prime_check(q)
    while check_q == False:
        print("q is not prime.")
        q = int(input("Enter a prime number for q: "))
        check_q = prime_check(q)

    #  Calculation of RSA modulus N
    n = p * q
    # print("RSA Modulus(n) is:", n)

    # Calculation of Eulers toitent 'r'
    r = (p-1)*(q-1)
    # print("Eulers Toitent(r) is:", r)
    # print("*****************************************************")

    # 'e' Value Calculation #
    e = int(input("Enter an exponent e between 1 and 1000: "))
    check_e = egcd(e, r)
    while check_e != 1:
        print("e is not valid.")
        p = int(input("Enter an exponent e between 1 and 1000: "))
        check_e = egcd(e, r)
    # print("The value of e is:", e)
    # print("*****************************************************")

    # d, Private and Public Keys #
    '''CALCULATION OF 'd', PRIVATE KEY, AND PUBLIC KEY.'''
    # print("EUCLID'S ALGORITHM:")
    eugcd(e, r)
    # print("END OF THE STEPS USED TO ACHIEVE EUCLID'S ALGORITHM.")
    # print("*****************************************************")
    # print("EUCLID'S EXTENDED ALGORITHM:")
    d = mult_inv(e, r)
    # print("END OF THE STEPS USED TO ACHIEVE THE VALUE OF 'd'.")
    # print("The value of d is:", d)
    # print("*****************************************************")
    public = (e, n)
    private = (d, n)
    print("Private Key is:", private)
    print("Public Key is:", public)
    # print("*****************************************************")

    # INPUT MESSAGE #
    message = input(
        "What would you like encrypted or decrypted? (Separate numbers with ',' for decryption):")
    # print("Your message is:", message)

    # Choose Encrypt or Decrypt and Print #
    method = input("Select 'encrypt' or 'decryt': ")
    if(method == 'encrypt'):
        enc_msg = encrypt(public, message)
        print("Your encrypted message is:", enc_msg)
        print("Thank you for using the RSA Encryptor. Goodbye!")
    elif(method == 'decryt'):
        print("Your decrypted message is:", decrypt(private, message))
        print("Thank you for using the RSA Encryptor. Goodbye!")


def main():
    rsa()
    
if __name__ == "__main__":
    main()
