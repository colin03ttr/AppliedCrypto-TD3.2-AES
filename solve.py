import base64
from Crypto.Cipher import AES

def pad(message):
    if len(message) % 16 != 0:
        message = message + '0' * (16 - len(message) % 16)  #block-size = 16
    return message

def encrypt(key, plain):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(plain)

def get_ciphertext(sitrep):
    message = '''sixteen byte AES{sitrep}{secret_code}'''.format(sitrep=sitrep, secret_code="FLAG{dummy_flag}")  # Fake flag for testing
    message = pad(message)
    message1 = bytes(message, 'utf-8')
    cipher = encrypt(b'sixteen byte key', message1)
    return base64.b64encode(cipher).decode('ascii')

# Given ciphertext for empty input
target_cipher = "xX+NDjg0X9tmJLobdQv9k3p8OAaf7GXlB81oPjRoqhA="
cipher_for_16A = "xX+NDjg0X9tmJLobdQv9k9VR6ytFTCy5JN+wlNbxGzR6fDgGn+xl5QfNaD40aKoQ"

# Step 1: Find block size (We assume it's 16 bytes from AES)
block_size = 16

# Step 2: Generate padding to shift flag into a known position
known_part = ""
while True:
    pad_length = block_size - (len(known_part) % block_size) - 1
    pad_input = "A" * pad_length
    cipher_base = get_ciphertext(pad_input)

    if cipher_base[:24] == target_cipher[:24]:  # Compare first encrypted blocks
        for c in range(32, 127):  # ASCII printable range
            test_input = pad_input + known_part + chr(c)
            cipher_test = get_ciphertext(test_input)
            if cipher_test[:24] == target_cipher[:24]:  # Compare matching blocks
                known_part += chr(c)
                print(f"Recovered so far: {known_part}")
                break
        else:
            break  # Stop if no match found (flag fully recovered)

print(f"Final Flag: {known_part}")
