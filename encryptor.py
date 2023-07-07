import os

def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()

    # Perform encryption
    encrypted_content = bytes([(byte + 1) % 256 for byte in content])

    # Create a new file with the encrypted content

    file_name = os.path.basename(file_path)
    file_name_without_extension, file_extension = os.path.splitext(file_name)
