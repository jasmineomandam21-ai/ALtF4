# 1-Month Cryptography Learning Roadmap

<br>

## Introduction

**Cryptography** is a core field in cybersecurity concerned with securing information through mathematical techniques. It focuses on protecting data confidentiality, integrity, authenticity, and non-repudiation against unauthorized access and manipulation. Modern cryptography underpins nearly all secure digital systems, including web security, authentication protocols, secure communication, and blockchain technologies.

This roadmap presents a **focused 1-month learning plan** designed to build a strong foundation in cryptography for beginners. 
The goal is to understand how cryptographic primitives work, why they are secure, how they are used in real systems, and how improper usage leads to vulnerabilities. Emphasis is placed on conceptual understanding, practical applications, and hands-on challenges.

---
<br>

## Week 1 — Cryptography Fundamentals and Classical Cryptography

**Goal:** Build a strong conceptual foundation and understand why cryptography is necessary.

_**Specific learning tasks:**_
- Learn the core goals of cryptography:
  - Confidentiality
  - Integrity
  - Authentication
  - Non-repudiation
- Understand basic cryptographic terminology:
  - Plaintext, ciphertext, key, encryption, decryption
- Study classical cryptographic algorithms:
  - Caesar cipher
  - Monoalphabetic substitution cipher
  - Vigenère cipher
- Learn basic cryptanalysis techniques:
  - Frequency analysis
  - Known-plaintext attacks
- Analyze why classical ciphers fail against modern attacks
---
_**Practical tasks:**_ <br>
  **1.)**  Encrypt and decrypt messages using Caesar and Vigenère ciphers<br>
   **2.)**  Perform frequency analysis to partially break a substitution cipher<br>
   **3.)**  Solve 1 classical-crypto CTF challenge (Caesar/Vigenère-based)<br>

---
<br>

## Week 2 — Symmetric Cryptography and Hash Functions

**Goal:** Understand how modern systems efficiently protect data and verify integrity.

_**Specific learning tasks:**_
- Learn symmetric-key cryptography concepts:
  - Shared secret keys
  - Block ciphers vs stream ciphers
- Study AES in detail:
  - Key sizes (128, 192, 256)
  - High-level structure (rounds, substitution, permutation)
- Learn block cipher modes of operation:
  - ECB, CBC, CTR, GCM
  - Understand why ECB is insecure
- Study cryptographic hash functions:
  - Properties (preimage resistance, collision resistance)
  - SHA-256 and SHA-3
- Learn message authentication mechanisms:
  - MAC
  - HMAC
---
_**Practical tasks:**_ <br>
 **1.)**  Use a crypto library to encrypt and decrypt data with AES<br>
 **2.)**  Compare ECB vs CBC (observe or explain the difference)<br>
 **3.)**  Generate a hash and HMAC and explain their use cases<br>
 **4.)**  Solve 1 symmetric-crypto CTF challenge<br>

---
<br>

## Week 3 — Asymmetric Cryptography and Key Management

**Goal:** Learn how secure key exchange and authentication work over insecure networks.

_**Specific learning tasks:**_
- Understand public-key cryptography:
  - Public and private keys
  - Key distribution problem
- Study RSA:
  - Mathematical principles (modular arithmetic, primes)
  - Key generation process
  - Encryption, decryption, and digital signatures
- Learn common RSA weaknesses:
  - Small public exponent attacks
  - Weak or reused primes
  - Improper padding
- Study key exchange mechanisms:
  - Diffie–Hellman
  - Elliptic Curve Diffie–Hellman (ECDH)
- Learn about digital certificates:
  - Certificate authorities (CA)
  - Certificate chains and trust models
---
_**Practical tasks:**_ <br>
**1.)**  Walk through RSA key generation and encryption (math + concept)<br>
**2.)**  Analyze one weak RSA scenario (e.g., small exponent or bad primes)<br>
**3.)**  Trace a TLS handshake and identify where asymmetric crypto is used<br>
**4.)**  Solve 1 public-key crypto CTF challenge<br>

---
<br>

## Week 4 — Applied Cryptography and Common Attacks

**Goal:** Apply cryptographic knowledge to real-world systems and identify insecure practices.

_**Specific learning tasks:**_
- Learn secure password storage techniques:
  - Salting
  - Key stretching
  - bcrypt, scrypt, and Argon2
- Study randomness and entropy:
  - Importance of secure random number generators
  - Common randomness failures
- Learn applied cryptography concepts:
  - HTTPS and TLS overview
  - Token-based authentication (JWT basics)
- Study common cryptographic attacks:
  - Brute-force attacks
  - Replay attacks
  - Chosen-plaintext attacks
  - Padding oracle attacks (conceptual understanding)
- Learn cryptographic best practices and secure design principles
---
_**Practical tasks:**_ <br>
**1.)**  Compare secure vs insecure password storage methods<br>
**2.)**  Analyze one real-world crypto misuse (e.g., ECB, bad JWT)<br>
**3.)**  Solve 1 applied-crypto CTF challenge<br>
**4.)**  Mini-project: <br>
   - Review a cryptographic system or protocol
   - Identify weaknesses or misuse
   - Propose more secure alternatives

---
<br>

## Expected Outcomes After 1 Month

By completing this roadmap, learners should be able to:
- Clearly explain fundamental cryptographic concepts and goals
- Correctly distinguish and apply symmetric and asymmetric cryptography
- Understand how AES, RSA, hashing, and key exchange are used in practice
- Identify common cryptographic vulnerabilities and misuse
- Solve beginner to intermediate cryptography challenges in CTF environments
- Critically assess cryptographic designs in real-world applications

_Advanced topics such as elliptic curve cryptography, post-quantum cryptography, and zero-knowledge proofs are recommended as follow-up areas of study._
