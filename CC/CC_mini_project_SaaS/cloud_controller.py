import os
from cryptography.fernet import Fernet

# Generate key
KEY = Fernet.generate_key()
cipher = Fernet(KEY)


# Encryption
def encrypt_file(filename):

    with open(filename, "rb") as f:
        data = f.read()

    encrypted = cipher.encrypt(data)

    enc_file = filename + ".enc"

    with open(enc_file, "wb") as f:
        f.write(encrypted)

    return enc_file


# Decryption
def decrypt_file(filename):

    with open(filename, "rb") as f:
        data = f.read()

    decrypted = cipher.decrypt(data)

    output = "decrypted_" + filename.replace(".enc","")

    with open(output, "wb") as f:
        f.write(decrypted)

    return output


# Split File
def split_file(file):

    os.makedirs("cloud_storage", exist_ok=True)

    with open(file, "rb") as f:

        i = 0

        while True:

            chunk = f.read(1024 * 1024)

            if not chunk:
                break

            chunk_name = os.path.join("cloud_storage", f"{os.path.basename(file)}_part{i}")

            with open(chunk_name, "wb") as chunk_file:
                chunk_file.write(chunk)

            print("Created:", chunk_name)

            i += 1


# Merge File
def merge_file(filename):

    output_file = filename

    with open(output_file, "wb") as output:

        i = 0

        while True:

            part = os.path.join("cloud_storage", f"{filename}_part{i}")

            if not os.path.exists(part):
                break

            with open(part, "rb") as f:
                output.write(f.read())

            i += 1

    return output_file


# Upload Function
def upload(filename):

    print("Uploading file...")

    encrypted = encrypt_file(filename)

    print("Encrypted file:", encrypted)

    split_file(encrypted)

    print("File split completed")

    return "Upload Successful"


# Download Function
def download(filename):

    merged = merge_file(filename)

    decrypted = decrypt_file(merged)

    return decrypted