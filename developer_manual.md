# Developer’s Documentation:    

### A detailed developer log with progress: [meeting.md](https://github.com/missystem/crypto_learning_sys/blob/master/meeting.md)

## Overall explanation of this project:
* An interactive learning system for learning cryptosystems. 
* Help students who is learning cryptography, especially in the midst of the pandemic. 
* This web application is unique in that it uses interactive learning tools and communicates with the user at each step. 
* The user must input the correct number in each step to be able to reach the next step.

## This project is separated into 3 modules:
1. **Backend**
	- All Cryptosystem implementations are in [crypto_implementation](https://github.com/missystem/crypto_learning_sys/tree/master/crypto_implementation)
	- RSA 
	- Elgamal
	- The backend is responsible for creating and running the cryptosystems.
		- Each cryptosystem will return a list of string with corresponding numbers
		- These lists will be different in case of an error. More info can be found in the comments of each cryptosystem.

2. **Frontend** -- Input page and method portion
		- This section uses HTML, JavaScript, and CSS for the page design. In addition, it uses flask to call the backend module.

3. **Frontend** -- Interactive portion
		- This section uses JavaScript and JQuery calls to create an interactive module that interacts with the user.

**TESTING**    
Our testing had 4 stages:    
1. backend testing
	- We tested the backend section by running the code on different large and small numbers and made sure all outputs were correct. We used edge cases and normal ones to make sure the backend is functioning correctly and without any errors.
2. frontend -- input and method
	- How did Xuehai test
3. frontend -- Interactive portion
	- How did John test
4. Outside testing
	- We had friends who are not computer scientists and have no knowledge of cryptosystems test our product and give us some feedback about the accessibility, the instructions, and how to make out product better.







