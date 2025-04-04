def read(file_name: str) -> str:
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        return f"Файл {file_name} не найден!"
    except Exception as e:
        return f"Ошибка при чтении файла {file_name}: {e}"


def write(file_name: str, text: str):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        print(f"Ошибка при записи в файл {file_name}: {e}")
