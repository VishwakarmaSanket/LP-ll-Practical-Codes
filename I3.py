# Simple Block Cipher (DES-like demo without external packages)

# Helper: pad message to multiple of block size
def pad_message(message, block_size=8):
    padding_len = block_size - (len(message) % block_size)
    return message + chr(padding_len) * padding_len

# Helper: unpad message
def unpad_message(message):
    padding_len = ord(message[-1])
    return message[:-padding_len]

# Encryption: XOR each block with key
def encrypt_message(message, key):
    block_size = len(key)
    message = pad_message(message, block_size)
    ciphertext = ""

    for i in range(0, len(message), block_size):
        block = message[i:i+block_size]
        encrypted_block = "".join(
            chr(ord(block[j]) ^ ord(key[j])) for j in range(block_size)
        )
        ciphertext += encrypted_block
    return ciphertext

# Decryption: same XOR operation
def decrypt_message(ciphertext, key):
    block_size = len(key)
    plaintext = ""

    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i+block_size]
        decrypted_block = "".join(
            chr(ord(block[j]) ^ ord(key[j])) for j in range(block_size)
        )
        plaintext += decrypted_block
    return unpad_message(plaintext)

# Driver code
key = "8bytekey"   # must be 8 characters
plaintext = input("Enter Plain Text: ")

ciphertext = encrypt_message(plaintext, key)
print("Encrypted Text:", ciphertext.encode())  # show bytes-like output

decrypted_text = decrypt_message(ciphertext, key)
print("Decrypted Text:", decrypted_text)
