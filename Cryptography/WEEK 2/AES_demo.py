from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Step 1: Generate key and IV (the key is a AES-256 key, which is 32 bytes, and the IV is 16 bytes for AES)
key = os.urandom(32)
iv = os.urandom(16)

# Step 2: Create cipher
cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
encryptor = cipher.encryptor()
decryptor = cipher.decryptor()

# Step 3: Encrypt plaintext
plaintext = b"Hello AES!"
ciphertext = encryptor.update(plaintext) + encryptor.finalize()

# Step 4: Decrypt ciphertext
decrypted = decryptor.update(ciphertext) + decryptor.finalize()

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted)
