import os

def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()

    # Perform encryption
    encrypted_content = bytes([(byte + 1) % 256 for byte in content])
