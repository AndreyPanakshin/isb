import argparse
import os.path
from hybrid import HybridCryptoSystem
from const import USER_SETTINGS_FILE, ROOT_DIR
from fileshandler import FilesHandler

def parse_mode_argument() -> str:
    parser = argparse.ArgumentParser(description="Hybrid cryptosystem CLI.")
    parser.add_argument(
        "-m", "--mode",
        type=str,
        choices=["generate", "encrypt", "decrypt"],
        required=True,
        help="Mode: generate (keys), encrypt (text), decrypt (text)"
    )
    return parser.parse_args().mode

def main() -> None:
    try:
        settings = FilesHandler.get_json(USER_SETTINGS_FILE)
        for name, path in settings.items():
            settings[name] = os.path.join(ROOT_DIR, path)

        crypto = HybridCryptoSystem()
        mode = parse_mode_argument()

        if mode == "generate":
            crypto.create_all_keys(settings["public_key"],
                                   settings["private_key"],
                                   settings["symmetric_key"])
            print("Keys generated successfully.")
        elif mode == "encrypt":
            crypto.encrypt_text_file(settings["plain_text"],
                                     settings["private_key"],
                                     settings["symmetric_key"],
                                     settings["encrypted_text"])
            print("File encrypted successfully.")
        elif mode == "decrypt":
            crypto.decrypt_text_file(settings["encrypted_text"],
                                     settings["private_key"],
                                     settings["symmetric_key"],
                                     settings["decrypted_text"])
            print("File decrypted successfully.")
    except Exception as e:
        print(f"[Error] {e}")

if __name__ == "__main__":
    main()
