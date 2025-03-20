import binascii

# Intercepted message (hex)
hex_message = "1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f63731a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60"

# Convert hex to bytes
ciphertext = binascii.unhexlify(hex_message)

# Known plaintext ("ORDER:")
plaintext_header = b"ORDER:"

# Extract the repeating XOR key from the known plaintext
key = bytes([ciphertext[i] ^ plaintext_header[i] for i in range(len(plaintext_header))])

# Decrypt the message using the repeating XOR key
decrypted_message = bytes([ciphertext[i] ^ key[i % len(key)] for i in range(len(ciphertext))])

# Convert to readable text
decrypted_text = decrypted_message.decode(errors="ignore")
decrypted_text
