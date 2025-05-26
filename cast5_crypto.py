import os
from cryptography.hazmat.decrepit.ciphers import algorithms
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from fileshandler import FilesHandler

class CAST5Crypto:
    """Performs CAST5-based encryption and decryption."""

    def __init__(self):
        self.key = None

    def create_random_key(self, length_bits: int) -> None:
        if not (40 <= length_bits <= 128):
            raise ValueError("Invalid CAST5 key length. Must be between 40 and 128 bits.")
        self.key = os.urandom(length_bits // 8)

    def save_key(self, path: str) -> None:
        if not self.key:
            raise ValueError("Symmetric key not generated.")
        FilesHandler.write_bytes(path, self.key)

    def load_key(self, path: str) -> bytes:
        self.key = FilesHandler.get_bytes(path)
        return self.key

    def encrypt_file_content(self, input_path: str, output_path: str) -> None:
        try:
            plaintext = FilesHandler.get_bytes(input_path)
            padder = padding.PKCS7(64).padder()
            padded = padder.update(plaintext) + padder.finalize()
            iv = os.urandom(8)
            cipher = Cipher(algorithms.CAST5(self.key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(padded) + encryptor.finalize()
            FilesHandler.write_bytes(output_path, iv + ciphertext)
        except Exception as e:
            raise RuntimeError(f"Encryption failed: {e}")

    def decrypt_file_content(self, input_path: str, output_path: str) -> str:
        try:
            encrypted_data = FilesHandler.get_bytes(input_path)
            iv = encrypted_data[:8]
            ciphertext = encrypted_data[8:]
            cipher = Cipher(algorithms.CAST5(self.key), modes.CBC(iv))
            decryptor = cipher.decryptor()
            padded_plain = decryptor.update(ciphertext) + decryptor.finalize()
            unpadder = padding.PKCS7(64).unpadder()
            plain = unpadder.update(padded_plain) + unpadder.finalize()
            try:
                decoded = plain.decode('utf-8')
            except UnicodeDecodeError:
                decoded = plain.decode('utf-8', errors='replace')
            FilesHandler.write_txt(output_path, decoded)
            return decoded
        except Exception as e:
            raise RuntimeError(f"Decryption failed: {e}")
