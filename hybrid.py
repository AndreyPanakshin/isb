from rsa_crypto import RSACrypto
from cast5_crypto import CAST5Crypto

class HybridCryptoSystem:

    def __init__(self, key_length=128):
        self.symmetric = CAST5Crypto()
        self.asymmetric = RSACrypto()
        self.key_len = key_length

    def create_all_keys(self, pub_path: str, priv_path: str, enc_sym_path: str) -> None:
        try:
            self.asymmetric.create_rsa_keys()
            self.asymmetric.save_public_key(pub_path)
            self.asymmetric.save_private_key(priv_path)
            self.symmetric.create_random_key(self.key_len)
            self.asymmetric.encrypt_data_key(pub_path, self.symmetric.key, enc_sym_path)
        except Exception as e:
            raise RuntimeError(f"Key generation failed: {e}")

    def encrypt_text_file(self, input_txt: str, priv_path: str, enc_sym_path: str, output_encrypted: str) -> None:
        try:
            self.symmetric.key = self.asymmetric.decrypt_data_key(priv_path, enc_sym_path)
            self.symmetric.encrypt_file_content(input_txt, output_encrypted)
        except Exception as e:
            raise RuntimeError(f"Encryption process failed: {e}")

    def decrypt_text_file(self, encrypted_txt: str, priv_path: str, enc_sym_path: str, output_decrypted: str) -> None:
        try:
            self.symmetric.key = self.asymmetric.decrypt_data_key(priv_path, enc_sym_path)
            self.symmetric.decrypt_file_content(encrypted_txt, output_decrypted)
        except Exception as e:
            raise RuntimeError(f"Decryption process failed: {e}")
