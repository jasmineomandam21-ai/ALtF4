from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import binascii

# Step 1: Generate AES-256 key (32 bytes) and IV (16 bytes)
key = os.urandom(32)
iv = os.urandom(16)

# Step 2: Create cipher object using CFB mode
cipher = Cipher(algorithms.AES(key), modes.CFB(iv))

encryptor = cipher.encryptor()
decryptor = cipher.decryptor()

# Step 3: Define plaintext
plaintext = b"Hello AES!"

# Step 4: Encrypt
ciphertext = encryptor.update(plaintext) + encryptor.finalize()

# Step 5: Decrypt
decrypted = decryptor.update(ciphertext) + decryptor.finalize()

print("Key:", binascii.hexlify(key))
print("IV:", binascii.hexlify(iv))

print("\nPlaintext:", plaintext)
print("Ciphertext (hex):", binascii.hexlify(ciphertext))
print("Decrypted:", decrypted)

print("\nPlaintext Length:", len(plaintext))
print("Ciphertext Length:", len(ciphertext))