import os

def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()

    # Perform encryption
    encrypted_content = bytes([(byte + 1) % 256 for byte in content])

    # Create a new file with the encrypted content

    file_name = os.path.basename(file_path)
    file_name_without_extension, file_extension = os.path.splitext(file_name)
    encrypted_file_path = f"{file_name_without_extension}-encrypted{file_extension}"
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_content)

    print(f"Encryption complete. Encrypted file saved as {encrypted_file_path}")

def decrypt_file(file_path):
    with open(file_path, 'rb') as encrypted_file:
        encrypted_content = encrypted_file.read()

    # Perform decryption
    decrypted_content = bytes([(byte - 1) % 256 for byte in encrypted_content])

    # Create a new file with the decrypted content
    decrypted_file_path = file_path.replace('-encrypted', '-decrypted')
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_content)
