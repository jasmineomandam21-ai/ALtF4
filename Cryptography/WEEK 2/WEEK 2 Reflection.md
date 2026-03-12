# [*WEEK 2 REFLECTION* ]: **Symmetric Cryptography and Hash Functions**  
**Goal**: Understand how modern systems efficiently protect data and verify integrity.
<hr>

**TIME INVESTED:** 6 Hours and 45 Minutes  
**GOAL MET?:** Yes
<br>

**PRACTICAL TASKS COMPLETION:**
- [x] ***1.)**  Use a crypto library to encrypt and decrypt data with AES*  
- [x] ***2.)** Compare ECB vs CBC (observe or explain the difference)*  
- [x] ***3.)** Generate a hash and HMAC and explain their use cases*  
- [x] ***4.)** Solve 1 symmetric-crypto CTF challenge*
<br>

**OVERALL REFLECTION FOR WEEK 2** *(Learnings and Challenges)***:**  
Week 2 focused on the fundamental concepts of symmetric cryptography and hash functions, which are essential components of modern cybersecurity systems. Through the practical activities, I learned how symmetric encryption works using the Advanced Encryption Standard (AES) and how different modes of operation, such as ECB, CBC, and CFB, affect the security of encrypted data. Implementing these modes in Python allowed me to observe how plaintext is transformed into ciphertext and later restored through decryption when the correct key and parameters are used. I also explored cryptographic hashing using the SHA-256 algorithm and generated HMAC values, which helped me understand how hash functions ensure data integrity while HMAC adds authentication through the use of a secret key.

Another important learning experience during this week was solving a cryptography challenge from picoCTF, specifically the Guess My Cheese Part 2 challenge. This task involved analyzing how SHA-256 hashes were generated using a salted input and applying a rainbow table approach to recover the original values. By writing a Python script that generated hashes for all possible combinations of cheeses and two-character hexadecimal salts, I was able to identify the correct cheese and salt that produced the given hash.

One challenge I encountered was initially figuring out how to properly use the picoCTF webshell environment. At first, navigating the interface and executing commands was confusing, which slowed down my progress in interacting with the challenge files. However, after experimenting with the environment and becoming more familiar with the command-line workflow, I was eventually able to manage the tasks more efficiently and successfully complete the challenge.

Overall, Week 2 helped me connect theoretical concepts of symmetric cryptography and hash functions with practical implementations. The activities demonstrated how encryption protects confidentiality, while hashing mechanisms help maintain integrity and authentication. These experiences reinforced the importance of understanding both the algorithms themselves and how they are applied in real-world security systems.