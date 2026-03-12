import hashlib
import hmac
import binascii

# Step 1: Define the message
message = b"Cybersecurity is important"

# Step 2: Generate SHA-256 hash
hash_object = hashlib.sha256(message)
hash_digest = hash_object.digest()

# Step 3: Define a secret key for HMAC
key = b"super_secret_key"

# Step 4: Generate HMAC using SHA-256
hmac_object = hmac.new(key, message, hashlib.sha256)
hmac_digest = hmac_object.digest()

# Step 5: Display results
print("Message:", message)

print("\nSHA-256 Hash:", binascii.hexlify(hash_digest))

print("\nSecret Key:", key)
print("HMAC-SHA256:", binascii.hexlify(hmac_digest))