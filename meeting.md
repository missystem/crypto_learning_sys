# Project 2
---

## Meeting Schedules:
* Monday: 4pm - 6pm
* Friday: 11am - 1pm
* Saturday as needed
---

## Separate this project into 3 sections:
1. Front end (JAVA script - JQuery)
	- detailed solution page
2. Middle part (html, flask)
	- initial page
	- "just show result"
3. Back end (python code - crypto algorithm)
	- Look into cryptosys and find the desired variables that are needed for encryption/decryption

---

## Group Members: Donna Hooshmand, Xuehai Zhou, John Zhou, Missy Shi
* **Donna**: Documentations (meetings & Schedule)
* **John**: Documentations
* **Xuehai**: Tester
* **Missy**: Repo manager

---

### 10/28 W
* Task Assignments:
	* Java Script & Jquery:
		- John
	* html & flask:
		- Xuehai
		- Donna
	* Python
		- Missy
		- Donna

* Website pages:
	1. Initial Page:
		1. Welcome message + Product info + User manual
		2. Select cryptosystem
		3. encrypt/decrypt
	2. Give the variables related to the cryptosystem (different versions based on the cryptosystem)
	3. Interactive page

* TODO (until Friday)
	- Find cryptosystems to do and give info on them - Donna & Missy
		- How many? Which one?
	 	- Give variables we would need on the webpage
	- Learn Flask & html - Xuehai & Donna
	- Create a temporary timeline for project - Donna
	- Learn JavaScript and Jquery - John


---

### 10/29 Th: Donna and Missy
* Which cryptosystems to use:
	* The RSA Cryptosystem 
		- Key creation:
			- Choose secret primes p and q
			- Choose encryption exponent e wih gcd(e,(p-1)(q-1)) = 1
			- Publish N = pq and e.
		- Encryption:
			- Choose plaintext m
			- Use Bob's public key (N, e) to compute c≡ m^e (mod N)
			- Send ciphertext c to Bob.
		- Decryption:
			- Compute d satisying ed≡1(mod(p-1)(q-1))
			- Compute m'≡c^d (mod N)
			- Then m' equals the plaintext.
	- Diffie-Hellman Key Exchange
		- SC please
	- ElGamal Key Creation 
		- sc pleasehlig-Hellman
	- Po
	- Vigenere Cipher (?)
	- Substitution Cipher (?)
	- DES (?)
	- AES (?)

