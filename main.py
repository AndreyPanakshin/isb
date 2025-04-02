def method_atbash(original_text: str, alphabet_upper: str, alphabet_lower: str) -> str:
    try:
        if not original_text or not alphabet_upper or not alphabet_lower:
            return "Отсутствует текст или алфавит"

        encrypted_text = ""
        for let in text:
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


def read_file(file_name: str) -> str:
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Файл {file_name} не найден!"
    except Exception as e:
        return f"Ошибка при чтении файла {file_name}: {e}"


def write_file(file_name: str, text: str):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        print(f"Ошибка при записи в файл {file_name}: {e}")


if __name__ == '__main__':
    text_file = 'original.txt'
    alphabet_file = 'alphabet.txt'

    text = read_file(text_file)
    alphabet = read_file(alphabet_file)

    if text.startswith("Ошибка") or alphabet.startswith("Ошибка"):
        print(text if text.startswith("Ошибка") else alphabet)
    else:
        alphabet_upper = ''.join([char for char in alphabet if char.isupper()])
        alphabet_lower = ''.join([char for char in alphabet if char.islower()])

        encrypted_text = method_atbash(text, alphabet_upper,alphabet_lower)

        write_file('encoded.txt', encrypted_text)

        print("Шифрование завершено. Зашифрованный текст сохранен в 'encoded_message.txt'.")
