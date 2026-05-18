import os
from cryptography.fernet import Fernet

# Récupération de la clé depuis GitHub Secrets
key = os.environ["FERNET_KEY"]

# Initialisation Fernet
fernet = Fernet(key.encode())

def encrypt_file(input_file, output_file):
    with open(input_file, "rb") as f:
        data = f.read()

    encrypted_data = fernet.encrypt(data)

    with open(output_file, "wb") as f:
        f.write(encrypted_data)

    print(f"Fichier chiffré : {output_file}")

def decrypt_file(input_file, output_file):
    with open(input_file, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(output_file, "wb") as f:
        f.write(decrypted_data)

    print(f"Fichier déchiffré : {output_file}")

if __name__ == "__main__":

    # Chiffrement
    encrypt_file("secretAt1.txt", "secretAt1.enc")

    # Déchiffrement
    decrypt_file("secretAt1.enc", "secretAt1.dec.txt")