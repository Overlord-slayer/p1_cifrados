from Crypto.Cipher import ARC4
import binascii

# Clave (reemplázala por la correcta)
key = b'211024'

# Texto cifrado en hex
ciphertext_hex = "c5c698284ebf7b97371a0e693bc84a6fd1bb76346e9dc6d62d0dffe5b8f06d16d53b3d1967"
ciphertext = bytes.fromhex(ciphertext_hex)

# Desencriptar
cipher = ARC4.new(key)
plaintext = cipher.decrypt(ciphertext)

print(plaintext.decode(errors="ignore"))  # usa 'ignore' por si hay caracteres raros
