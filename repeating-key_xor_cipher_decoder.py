import binascii

# Intercepted message (hex)
hex_message = "1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f63731a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60"

# Convert hex to bytes
ciphertext = binascii.unhexlify(hex_message)

# Known plaintext ("ORDER:")
plaintext_header = b"ORDER:"

# Extract the repeating XOR key from the known plaintext
key = bytes([ciphertext[i] ^ plaintext_header[i] for i in range(len(plaintext_header))])

# Function to decrypt with repeating-key XOR
def xor_decrypt(ciphertext, key):
    key_length = len(key)
    return bytes([ciphertext[i] ^ key[i % key_length] for i in range(len(ciphertext))])

# Decrypt the message using the extracted key
decrypted_message = xor_decrypt(ciphertext, key)

# Convert decrypted bytes to readable text
print(decrypted_message.decode(errors='ignore'))
