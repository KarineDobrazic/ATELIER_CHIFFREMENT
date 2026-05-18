import os
import base64
from nacl.secret import SecretBox

# Récupération de la clé depuis GitHub Secrets
key_b64 = os.environ["SECRETBOX_KEY"]

# Conversion Base64 -> bytes
key = base64.b64decode(key_b64)

# Initialisation SecretBox
box = SecretBox(key)

# Fonction de chiffrement
def encrypt_file(input_file, output_file):

    with open(input_file, "rb") as f:
        data = f.read()

    encrypted = box.encrypt(data)

    with open(output_file, "wb") as f:
        f.write(encrypted)

    print(f"Fichier chiffré : {output_file}")

# Fonction de déchiffrement
def decrypt_file(input_file, output_file):

    with open(input_file, "rb") as f:
        encrypted_data = f.read()

    decrypted = box.decrypt(encrypted_data)

    with open(output_file, "wb") as f:
        f.write(decrypted)

    print(f"Fichier déchiffré : {output_file}")

# Programme principal
if __name__ == "__main__":

    encrypt_file("secretAt2.txt", "secretAt2.enc")

    decrypt_file("secretAt2.enc", "secretAt2.dec.txt")