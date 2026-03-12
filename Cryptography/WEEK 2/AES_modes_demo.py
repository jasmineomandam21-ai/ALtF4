from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os
import binascii

# 16-byte key for AES-128
key = b"aesEncryptionKey"

# Random IV for CBC
iv = os.urandom(16)

# Plaintext with repeating 16-byte blocks (important for ECB demo)
plaintext = b"HELLO_AES_BLOCK!" * 4

print("Plaintext:", plaintext)

padder = padding.PKCS7(128).padder()
padded_plaintext = padder.update(plaintext) + padder.finalize()

# ---------------- ECB MODE ----------------
cipher_ecb = Cipher(algorithms.AES(key), modes.ECB())
encryptor_ecb = cipher_ecb.encryptor()

ciphertext_ecb = encryptor_ecb.update(padded_plaintext) + encryptor_ecb.finalize()

decryptor_ecb = cipher_ecb.decryptor()
decrypted_padded_ecb = decryptor_ecb.update(ciphertext_ecb) + decryptor_ecb.finalize()

unpadder = padding.PKCS7(128).unpadder()
decrypted_ecb = unpadder.update(decrypted_padded_ecb) + unpadder.finalize()

print("\nECB Ciphertext:", binascii.hexlify(ciphertext_ecb))
print("ECB Decrypted:", decrypted_ecb)

# ---------------- CBC MODE ----------------
cipher_cbc = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor_cbc = cipher_cbc.encryptor()

ciphertext_cbc = encryptor_cbc.update(padded_plaintext) + encryptor_cbc.finalize()

decryptor_cbc = cipher_cbc.decryptor()
decrypted_padded_cbc = decryptor_cbc.update(ciphertext_cbc) + decryptor_cbc.finalize()

unpadder = padding.PKCS7(128).unpadder()
decrypted_cbc = unpadder.update(decrypted_padded_cbc) + unpadder.finalize()

print("\nCBC Ciphertext:", binascii.hexlify(ciphertext_cbc))
print("CBC Decrypted:", decrypted_cbc)