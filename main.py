import config
import read as r

def method_atbash(original_text: str, alphabet_upper: str, alphabet_lower: str) -> str:
    try:
        if not original_text or not alphabet_upper or not alphabet_lower:
            return "Отсутствует текст или алфавит"

        encrypted_text = ""
        for let in original_text:
            if let.isupper() and let in alphabet_upper:
                i = alphabet_upper.index(let)
                encrypted_text += alphabet_upper[-i - 1]
            elif let.islower() and let in alphabet_lower:
                i = alphabet_lower.index(let)
                encrypted_text += alphabet_lower[-i - 1]
            else:
                encrypted_text += let
        return encrypted_text

    except Exception as e:
        return f"Ошибка: {e}"


if __name__ == '__main__':
    text = r.read(config.TEXT_FILE)
    alphabet = r.read(config.ALPHABET_FILE)

    if text.startswith("Ошибка") or alphabet.startswith("Ошибка"):
        print(text if text.startswith("Ошибка") else alphabet)
    else:
        alphabet_upper = ''.join([char for char in alphabet if char.isupper()])
        alphabet_lower = ''.join([char for char in alphabet if char.islower()])

        encrypted_text = method_atbash(text, alphabet_upper,alphabet_lower)

        r.write(config.ENCRYPTED_TEXT_FILE, encrypted_text)

        print("Шифрование завершено. Зашифрованный текст сохранен в 'encoded_message.txt'.")
