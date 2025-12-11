# Import modules
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Encryption / decryption constants
SALT_SIZE = 16
NONCE_SIZE = 12
KEY_LENGTH = 32
PBKDF2_ITERATIONS = 1000000


def __derive_key(master_password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_LENGTH,
        salt=salt,
        iterations=PBKDF2_ITERATIONS,
        backend=default_backend()
    )
    return kdf.derive(master_password.encode("utf-8"))


def encrypt(plaintext: str, master_password: str = "") -> str:
    salt = os.urandom(SALT_SIZE)
    nonce = os.urandom(NONCE_SIZE)

    key = __derive_key(master_password, salt)

    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode("utf-8")) + encryptor.finalize()
    tag = encryptor.tag

    encrypted_data = salt + nonce + tag + ciphertext

    return base64.b64encode(encrypted_data).decode("ascii")


def decrypt(encrypted_b64: str, master_password: str = "") -> str:
    data = base64.b64decode(encrypted_b64)

    salt = data[:SALT_SIZE]
    nonce = data[SALT_SIZE:SALT_SIZE + NONCE_SIZE]
    tag = data[SALT_SIZE + NONCE_SIZE:SALT_SIZE + NONCE_SIZE + 16]
    ciphertext = data[SALT_SIZE + NONCE_SIZE + 16:]

    key = __derive_key(master_password, salt)

    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    return plaintext.decode("utf-8")
