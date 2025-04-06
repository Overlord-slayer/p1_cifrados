from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes  # pycryptodome
from binascii import unhexlify


def generate_key_nonce(user_id):
    key = (user_id.encode() * 32)[:32]  # Derivar clave de 256 bits del ID
    nonce = (user_id.encode() * 8)[:8]  # Derivar nonce de 64 bits del ID
    return key, nonce


def chacha20_encrypt(plaintext, user_id):
    key, nonce = generate_key_nonce(user_id="1234")
    cipher = ChaCha20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext


def chacha20_decrypt(ciphertext, user_id):
    key, nonce = generate_key_nonce(user_id="1234")
    cipher = ChaCha20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode()


def nami_cipher(plaintext, user_id):
    ciphertext = chacha20_encrypt(plaintext, user_id)
    return ciphertext

text="3fc06ae08a1da3b0dfdd6cdf052435026360b73d778607f9c81ba4c5e3608269653ce10237"
text_bytes = unhexlify(text)
print(chacha20_decrypt(text_bytes, "211024"))