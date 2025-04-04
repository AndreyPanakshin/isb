import json
import os
import read as r
import config


def load_json(file_path: str) -> dict:
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл {file_path} не найден.")

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if not content:
                raise ValueError("Файл JSON пуст!")

            return json.loads(content)
    except json.JSONDecodeError:
        print(f"Ошибка: Файл {file_path} не является корректным JSON.")
        return {}
    except Exception as e:
        print(f"Ошибка загрузки JSON: {e}")
        return {}


def save_json(data: dict, file_path: str) -> None:
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ошибка сохранения JSON: {e}")


def analyze_frequency(text: str) -> dict[str, float]:

    total_chars = len(text)
    if total_chars == 0:
        return {}

    frequency = {char: text.count(char) / total_chars for char in set(text)}
    return dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))


def create_decryption_key(encrypted_freq: dict, reference_freq: dict) -> dict[str, str]:
    sorted_encrypted = sorted(encrypted_freq.keys(), key=lambda c: encrypted_freq[c], reverse=True)
    sorted_reference = sorted(reference_freq.keys(), key=lambda c: reference_freq[c], reverse=True)

    return {enc: ref for enc, ref in zip(sorted_encrypted, sorted_reference)}


def decrypt_text(text: str, key: dict[str, str]) -> str:
    return ''.join(key.get(char, char) for char in text)

if __name__ == "__main__":

    encrypted_text = r.read(config.ENCODED_TASK2_FILE)

    if not encrypted_text:
        print("Ошибка: зашифрованный текст отсутствует!")
        exit(1)


    reference_frequency = load_json(config.REFERENCE_FREQ_FILE)
    
    key_final=load_json(config.FINAL_KEY_FILE)


    if not reference_frequency:
        print("Ошибка: не удалось загрузить частотный анализ языка!")
        exit(1)

    encrypted_frequency = analyze_frequency(encrypted_text)

    save_json(encrypted_frequency, config.ENCRYPTED_FREQ_FILE)

    decryption_key = create_decryption_key(encrypted_frequency,reference_frequency)


    decrypted_text = decrypt_text(encrypted_text, key_final)


    save_json(decryption_key, config.DECRYPTION_KEY_FILE)
    r.write(decrypted_text, config.DECRYPTED_TASK2_FILE)

    print("\n расшифровка завершена!")
    print("Ключ сохранен в:", config.DECRYPTION_KEY_FILE)
    print("расшифрованный текст сохранен в:", config.DECRYPTED_TASK2_FILE)
