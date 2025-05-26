from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from typing import Tuple
from fileshandler import FilesHandler

class RSACrypto:
    """Handles RSA key generation and encryption/decryption of symmetric keys."""

    def __init__(self):
        self.public_key = None
        self.private_key = None

    def create_rsa_keys(self) -> Tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.public_key = self.private_key.public_key()
        return self.public_key, self.private_key

    def save_public_key(self, path: str) -> None:
        if not self.public_key:
            raise ValueError("Public key not generated.")
        FilesHandler.write_public_key(path, self.public_key)

    def save_private_key(self, path: str) -> None:
        if not self.private_key:
            raise ValueError("Private key not generated.")
        FilesHandler.write_private_key(path, self.private_key)

    @staticmethod
    def load_public_key(path: str) -> rsa.RSAPublicKey:
        return FilesHandler.read_public_key(path)

    @staticmethod
    def load_private_key(path: str) -> rsa.RSAPrivateKey:
        return FilesHandler.read_private_key(path)

    def encrypt_data_key(self, public_key_path: str, data_key: bytes, output_path: str) -> bytes:
        try:
            public_key = self.load_public_key(public_key_path)
            encrypted_key = public_key.encrypt(data_key, padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(), label=None))
            FilesHandler.write_bytes(output_path, encrypted_key)
            return encrypted_key
        except Exception as e:
            raise RuntimeError(f"Failed to encrypt data key: {e}")

    def decrypt_data_key(self, private_key_path: str, encrypted_key_path: str) -> bytes:
        try:
            private_key = self.load_private_key(private_key_path)
            encrypted_key = FilesHandler.get_bytes(encrypted_key_path)
            return private_key.decrypt(encrypted_key, padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(), label=None))
        except Exception as e:
            raise RuntimeError(f"Failed to decrypt data key: {e}")
