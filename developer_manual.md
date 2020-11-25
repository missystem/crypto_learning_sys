# Developer’s Documentation:    

### A detailed developer log with progress: [meeting.md](https://github.com/missystem/crypto_learning_sys/blob/master/meeting.md)

---

## Overall explanation of this project:
* An interactive learning system for learning cryptosystems. 
* Help students who is learning cryptography, especially in the midst of the pandemic. 
* This web application is unique in that it uses interactive learning tools and communicates with the user at each step. 
* The user must input the correct number in each step to be able to reach the next step.

---

## General mapping of each directory in this repo:
* **README.md**
	- A user guide, give assistance to user who is using the cryptosystem interactive learning system

* **config**:
	- [Page Design](https://github.com/missystem/crypto_learning_sys/tree/master/config/Page%20Design): Page designs for each cryptosystem
	- [algorithm_info](https://github.com/missystem/crypto_learning_sys/tree/master/config/algorithm_info): Guide to the frontend developers
		- examples and methods used for each cryptosystem
	- config.sh: used by users to download the required libraries
		- used in heroku to set up the environment

* **images**:
	- images inserted in each .md file

* **meeting.md**
	- Detailed developers' log
		-includes progress for each week in addition to any obstacles we faced
* **crypto_implementation**
	- cryptosystem implementations
* **templates**
	- the mainpage is stored here. This is the file for all frontend functionality.
* **static**
	- design elements of the main page (css).

---

### This project is separated into 3 modules:
1. **Back-End**
	- Cryptosystem implementations
	- Creating and running the cryptosystems.
		- Each cryptosystem will return a list of string with corresponding numbers
		- These lists are different for different cryptosystems. 
		- Frontend takes output list to make interactive process
		- Detailed explanation in the comments of each cryptosystem implementation
			- [RSA Key Exchange]((https://github.com/missystem/crypto_learning_sys/blob/master/crypto_implementation/RSA.py)	
			- [Diffie-Hellman Key Exchange](https://github.com/missystem/crypto_learning_sys/blob/master/crypto_implementation/DH.py)
			- [Elgamal Public Key Cryptosystem](https://github.com/missystem/crypto_learning_sys/blob/master/crypto_implementation/Elgamal.py)

2. **Front-End** 
	- Input page and method portion
	- HTML, JavaScript, CSS for the page design. 
	- Use Flask to run backend.

3. **Middle-End** 
	- Interactive portion
	- JavaScript and JQuery calls to create an interactive module that interacts with the user.


### TESTING  
1. backend testing
	- Use test file [temptest.py](https://github.com/missystem/crypto_learning_sys/blob/master/crypto_implementation/temptest.py) to run each program with random generated data sets
2. frontend -- input and method
	- Various tests to make sure html, flask, and the backend portion are working well together.
3. frontend -- Interactive portion
	- Before merging both frontend sections, Ajax code and calls were tested to make sure everthing is correct.
4. frontend -- "full frontend"
	- Tried small numberes in addition to very large number (more than 10 digits), in addition to edge cases such as inputing non prime numbers, and incorrect numbers.
5. Product testing
	- Invited people to try our learning system and give us feedback about the accessibility, the instructions, and what to improve

### Further Extensions:
* Adding more cryptosystems
	- You would have to 
		- make the corresponding changes in ​Frontend code​ to add them to the main page
		- make the corresponding changes in Middleend code​ ​to add the javascript and jquery calls, in addition to construct the new cryptosystem
	- Creating app for iOS or Android
	- Make it compatible with screen readers
	- Adding video or voice explanation option that can walk through the methods and examples








