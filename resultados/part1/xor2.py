def xor_decrypt(hex_data, key):
    data = bytes.fromhex(hex_data)  # Convertir hex a bytes
    key = key.encode()  # Convertir clave a bytes
    decrypted = bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])
    return decrypted.decode(errors="ignore")  # Intentar decodificar a texto

# Extraer solo la parte hexadecimal después de "FLAG_"
hex_string = "0a16e1e85da2dc414b4447cd580d63f3"

# Tu carné (reemplázalo con el tuyo)
carnet = "123456"

# Intentar descifrar
flag_descifrada = xor_decrypt(hex_string, carnet)
print("FLAG_" + flag_descifrada)
